from django.urls import path, include
from .views import *


urlpatterns = [
    
    path('home/', home), #the function home is called here
    path('index/', index),#the function index is called here 
    path('contact/', contact),
    path('about/', about),
]