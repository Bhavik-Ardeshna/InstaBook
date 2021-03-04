from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . import models
from django.contrib.auth.models import User
from . import forms
from django.core.paginator import Paginator
from django.urls import resolve

from django.contrib.auth.decorators import login_required
from post.models import Post, Follow, Stream


@login_required
def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile = models.Profile.objects.get(user=user)
    url_name = resolve(request.path).url_name

    if url_name == 'profile':
        posts = Post.objects.filter(user=user).order_by('-posted')

    else:
        posts = profile.favorites.all()

    posts_count = Post.objects.filter(user=user).count()
    following_count = Follow.objects.filter(follower=user).count()
    followers_count = Follow.objects.filter(following=user).count()

    follow_status = Follow.objects.filter(
        following=user, follower=request.user).exists()

    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    context = {
        'posts': posts_paginator,
        'profile': profile,
        'following_count': following_count,
        'followers_count': followers_count,
        'posts_count': posts_count,
        'follow_status': follow_status,
        'url_name': url_name,
    }

    return render(request, 'profile.html', context)


def SignView(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            print("You are Signed up, Plz Login!")
            return redirect('account:login')
        else:
            print("Plz SigneUp again!")
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': form})


def LoginView(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.success(request,'Successfully Logged In')
                return redirect('post:index')
            # else:
                # messages.warning(request,"Invalid Username or Password")
    else:
        form = forms.LoginForm()
    return render(request, 'login.html', {'form': form})


def SignOutView(request):
    logout(request)
    return redirect('account:login')
