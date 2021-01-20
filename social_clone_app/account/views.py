from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from . import models
from django.contrib.auth.models import User

from . import forms


def SignView(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request,"You are Signed up, Plz Login!")
            return redirect('account:login')
        # else:
            # messages.error(request,"Plz SigneUp again!")
    else:
        form = forms.SignUpForm()
    return render(request,'signup.html',{'form':form})

def LoginView(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                # messages.success(request,'Successfully Logged In')
                return redirect('post:index')
            # else:
                # messages.warning(request,"Invalid Username or Password")
    else:
        form = forms.LoginForm()
    return render(request,'login.html',{'form':form})


def SignOutView(request):
    logout(request)
    return redirect('account:login')
