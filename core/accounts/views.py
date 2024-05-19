from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'
