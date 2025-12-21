from django.urls import path
from . import views


# app_name = 'frontend'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('buy/', views.contact, name='buy'),
    path('dealerships/', views.contact, name='dealerships'),
    path('showroom/', views.contact, name='showroom'),
]