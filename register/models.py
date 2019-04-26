# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class RegisterUser(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    admin = False
    date_registered = models.DateTimeField(default=timezone.now)  # auto_now_add=True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
