from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.template import loader
from .models import Product #importing the products class from models.py

# Create your views here.

def home(request):
    products = Product.objects.all() 
    context = {
        'prods' : products # the key 'peods' will be availabele to use in the django template desion
    } #context dictrionary for passing data for rendering
    template = loader.get_template('home.html')# creating a tempate object from the designed template ht
    return HttpResponse(template.render(context,request)) #creates a response object after rendering
#the returned response has the html of completed webpage including required data.
