from django.urls import path
from . import views


# app_name = 'frontend'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('buy/', views.buy, name='buy'),
    path('dealerships/', views.dealership, name='dealerships'),
    path('showroom/', views.showroom, name='showroom'),
]