from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.urls import reverse_lazy

from django.template import loader
from .models import Product #importing the products class from models.py

# importing necessary Generic class-based Views
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

# Create your views here.

def home(request):
    context = {}
    template = loader.get_template('home.html')# creating a tempate object from the designed template ht
    return HttpResponse(template.render(context,request)) 


def products(request):
    products = Product.objects.all() 
    context = {
        'prods' : products # the key 'peods' will be availabele to use in the django template desion
    } #context dictrionary for passing data for rendering
    template = loader.get_template('products.html')# creating a tempate object from the designed template ht
    return HttpResponse(template.render(context,request)) #creates a response object after rendering
#the returned response has the html of completed webpage including required data.

#view function for redering individual product page
def product_details(request,id):
    product = Product.objects.get(id = id)#select *from products where id = <parameter_id>
    context = {
        'prod' : product
    }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context,request))   

    # CRUD
#1. C - Create
class AddProduct(CreateView):
    model = Product
    fields = [
        'name',
        'price',
        'desc',
        'stock',
        'pic'
    ]
    template_name = 'addProduct.html'
    success_url = reverse_lazy('prod_page') #redirect to products page after adding product


    #2. R - reaad 
class ProductsView(ListView):
    model = Product
    tempate_name = 'productsView.html'
    ordering = ['-id'] # to sort in descending order

## search result

def searchView(request):
    query = request.GET.get('search_text')# fetch the query text GET request
    results = Product.objects.filter(name_icotains = query)# collect thr product objects mating the name
    context = {
        'items' : results,
        
    }

    tempate = loader.get_template('searchResults.html')
    return HttpResponse(tempate.render(context,request))
        #3. u - update

class EditProduct(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'editProduct.html'
    success_url = reverse_lazy('prod_page')

# 4. D - delete
class DelProduct(DeleteView):
    model = Product
    template_name = 'delProduct.html'
    success_url = reverse_lazy('homepage')
