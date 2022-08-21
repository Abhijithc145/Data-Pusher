from django.urls import path
from .import views
from .views import *


urlpatterns = [
    
    path('destination',destinations.as_view(),name='destination'),
    path('incoming_data',Incomingdata.as_view(),name='incoming_data'),
    path('getdestination/<str:pk>',Get_destination.as_view(),name='getdestination'),
    
]
