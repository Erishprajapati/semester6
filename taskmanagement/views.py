from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request): #logic that i need to show are written here
    return HttpResponse("Welcome Erish")

def index(request): #logic that i need to show are written here
    return HttpResponse("This is index function")

def contact(request):
    return HttpResponse("This is contact function")

def about(request): #logic that i need to show are written here
     return HttpResponse("This is about function")