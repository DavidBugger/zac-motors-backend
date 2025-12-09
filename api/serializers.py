from rest_framework import serializers
from .models import Car, Payment, Appointment, ContactMessage


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class PaymentSerializer(serializers.ModelSerializer):
    car_details = CarSerializer(source='car', read_only=True)
    
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['stripe_payment_intent_id', 'payment_date', 'status']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero.")
        return value


class AppointmentSerializer(serializers.ModelSerializer):
    car_details = CarSerializer(source='car', read_only=True)
    
    class Meta:
        model = Appointment
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'status']

    def validate_appointment_date(self, value):
        from django.utils import timezone
        if value < timezone.now():
            raise serializers.ValidationError("Appointment date cannot be in the past.")
        return value


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
        read_only_fields = ['created_at', 'is_read']
