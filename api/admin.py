from django.contrib import admin
from .models import Car, Payment, Appointment, ContactMessage


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['make', 'model', 'year', 'price', 'condition', 'is_available']
    list_filter = ['condition', 'is_available', 'make']
    search_fields = ['make', 'model', 'vin']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'car', 'amount', 'status', 'payment_date']
    list_filter = ['status', 'payment_date']
    search_fields = ['customer_name', 'customer_email']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'appointment_type', 'appointment_date', 'status']
    list_filter = ['status', 'appointment_type', 'appointment_date']
    search_fields = ['customer_name', 'customer_email']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']

