from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet, PaymentViewSet, AppointmentViewSet, ContactMessageViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'contact', ContactMessageViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
