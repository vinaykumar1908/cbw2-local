from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.homeView, name='home'),
    #path('charts/', include('charts.urls')),
    
]