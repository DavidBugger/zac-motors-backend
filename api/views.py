from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from .models import Car
import stripe
from rest_framework.decorators import action


from .models import Car, Payment, Appointment, ContactMessage
from .serializers import (
    CarSerializer, PaymentSerializer, 
    AppointmentSerializer, ContactMessageSerializer
)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        is_available = self.request.query_params.get('is_available', None)
        condition = self.request.query_params.get('condition', None)
        
        if is_available is not None:
            queryset = queryset.filter(is_available=is_available.lower() == 'true')
        if condition:
            queryset = queryset.filter(condition=condition)
            
        return queryset


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(detail=False, methods=['post'])
    def create_payment_intent(self, request):
        try:
            car_id = request.data.get('car_id')
            amount = request.data.get('amount')
            
            if not car_id or not amount:
                return Response(
                    {'error': 'car_id and amount are required'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            car = Car.objects.get(id=car_id)
            
            # Create Stripe payment intent
            intent = stripe.PaymentIntent.create(
                amount=int(float(amount) * 100),  # Convert to cents
                currency='usd',
                metadata={
                    'car_id': car_id,
                    'car_name': f"{car.year} {car.make} {car.model}"
                }
            )

            return Response({
                'client_secret': intent.client_secret,
                'payment_intent_id': intent.id
            })

        except Car.DoesNotExist:
            return Response(
                {'error': 'Car not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['post'])
    def confirm_payment(self, request):
        try:
            payment_intent_id = request.data.get('payment_intent_id')
            car_id = request.data.get('car_id')
            customer_name = request.data.get('customer_name')
            customer_email = request.data.get('customer_email')
            customer_phone = request.data.get('customer_phone')
            amount = request.data.get('amount')

            # Verify payment with Stripe
            intent = stripe.PaymentIntent.retrieve(payment_intent_id)

            if intent.status == 'succeeded':
                # Create payment record
                payment = Payment.objects.create(
                    car_id=car_id,
                    customer_name=customer_name,
                    customer_email=customer_email,
                    customer_phone=customer_phone,
                    amount=amount,
                    stripe_payment_intent_id=payment_intent_id,
                    status='completed'
                )

                # Mark car as unavailable
                car = Car.objects.get(id=car_id)
                car.is_available = False
                car.save()

                serializer = self.get_serializer(payment)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {'error': 'Payment not confirmed'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        status_filter = self.request.query_params.get('status', None)
        
        if status_filter:
            queryset = queryset.filter(status=status_filter)
            
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(
            {
                'message': 'Appointment booked successfully',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        appointment = self.get_object()
        appointment.status = 'confirmed'
        appointment.save()
        serializer = self.get_serializer(appointment)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        appointment = self.get_object()
        appointment.status = 'cancelled'
        appointment.save()
        serializer = self.get_serializer(appointment)
        return Response(serializer.data)


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(
            {
                'message': 'Message sent successfully',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED
        )
