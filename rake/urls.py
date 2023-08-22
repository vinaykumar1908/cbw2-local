from django.urls import path, include
from rake import views

urlpatterns = [
    path('', views.rakeView, name='rakehome'),
    
    ]