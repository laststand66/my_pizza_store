from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
class MainLogin(LoginView):
    template_name = 'profile_app/login.html'
