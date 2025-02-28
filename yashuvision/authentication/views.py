from django.shortcuts import render,redirect

#importing necessary modules for creating a class based view
from django.views import generic

#importing the form class from django's auth app
from django.contrib.auth.forms import UserCreationForm
#importing reverse_lazy to help with easy redirection back to logic page once registeration is complete
from django.urls import reverse_lazy

#django has an inbuilt view for login,let's import that
from django.contrib.auth.views import LoginView

# Create your views here.

#we will be implementing a class-based view instend of a
#function based view like we did with the first view in mainapp

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name ='registration.html'
    success_url = reverse_lazy('signin')
    #inheriting the loginview class
    
class Login(LoginView):
    template_name = 'login.html'