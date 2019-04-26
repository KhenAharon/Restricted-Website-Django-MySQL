from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'users': User.objects.all().first()
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html", {})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }

    return render(request, 'profile.html', context)