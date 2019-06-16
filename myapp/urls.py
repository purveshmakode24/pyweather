from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.weather, name='home-pyweather'),
    path('weather_details/', views.weather_details, name='weather_details'),
    path('error_404', views.error_404, name='error_404'),
]
