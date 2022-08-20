from django.urls import path
from .import views
from .views import *


urlpatterns = [
    
    path('create',Account_create.as_view(),name='create'),
    path('create/<int:pk>',Account_creates.as_view(),name='create'),
]
