from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.views import View
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import logging
# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'Register/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email_id = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(
                username=username, email=email_id, password=password)
            print(username, email_id, password)
        return render(request, 'Register/register.html', {'message': 'User created successfully'})


class LoginView(View):
    def get(self, request):
        return render(request, 'Register/login.html')

    def post(self, request):

        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                return render(request, 'Register/login.html', {'form': form, 'message': 'Invalid Credentials'})
        else:
            return render(request, 'Register/login.html', {'form': form})





class LogoutUser(View):
    def get(self, request):
        logout(request)
        return redirect('Register:login')
