from django.urls import path
from .import views
from .views import *


urlpatterns = [
    
    path('incoming_data',Incomingdata.as_view(),name='incoming_data'),
    
]
