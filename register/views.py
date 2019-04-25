from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    context = {
        'users': User.objects.all().first()
    }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html", {})
