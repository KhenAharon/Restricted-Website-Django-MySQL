from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, PasswordReset
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from .models import User, Profile
from django.contrib.auth.decorators import user_passes_test
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="khen",
  database="mydb",
  passwd="khen"
)

mycursor = mydb.cursor()


def login_success(request):
    if request.user.profile.login_counter == 0:
        request.user.profile.login_counter += 1
        request.user.save()
        return redirect("change_password")
    else:
        return redirect("home")


def home(request):
    if request.user.is_authenticated:
        context = {
            'users': User.objects.all().first(),
            'login_count': User.objects.filter(username=request.user).first().profile.login_counter
        }
    else:
        context = {
            'users': User.objects.all().first(),
            'login_count': 'unsigned'
        }
    return render(request, "home.html", context)


def about(request):
    return render(request, "about.html", {})


@user_passes_test(lambda u: u.is_superuser)
def edit_user2(request, id=0):
    user_to_update = User.objects.filter(id=id).first()

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user_to_update)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'This user has been updated!')
            return redirect('myadmin')
    else:
        u_form = UserUpdateForm(instance=user_to_update)

    context = {
        "id": id,
        'u_form': u_form
    }

    return render(request, "edituser.html", context)


@user_passes_test(lambda u: u.is_superuser)
def password_reset(request, id=0):
    user_to_update = User.objects.raw('SELECT * FROM auth_user WHERE id=' + str(id))
    user_to_update = user_to_update[0]  # there is only one such id, the user is in first index.

    if request.method == 'POST':

        form = PasswordChangeForm(user_to_update, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for encryption!
            messages.success(request, 'The password was successfully reset!')
            return redirect('myadmin')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user_to_update)
    return render(request, 'change_password.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def edit_user(request, id=0):
    user_to_update = User.objects.raw('SELECT * FROM auth_user WHERE id=' + str(id))
    user_to_update = user_to_update[0]  # there is only one such id, the user is in first index.

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=user_to_update)

        # updating the form by the POST method by the user.
        if u_form.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            admin = request.POST.get('is_superuser', '')

            if admin:
                admin = 1
            else:
                admin = 0

            sql = "UPDATE auth_user SET first_name ='" + first_name + "'," \
                  + "first_name ='" + first_name + "'," \
                  + "last_name ='" + last_name + "'," \
                  + "username ='" + username + "'," \
                  + "email ='" + email + "'," \
                  + "is_superuser ='" + str(admin) + "' " \
                  + "WHERE id=" + str(id)
            mycursor.execute(sql)
            mydb.commit()

            messages.success(request, f'This user has been updated!')
            return redirect('myadmin')
    else:
        # updating the view form, filling user fields from the db.
        u_form = UserUpdateForm(instance=user_to_update)

    context = {
        "id": id,
        'u_form': u_form
    }

    return render(request, "edituser.html", context)


'''
The decorator above with the lambda expression is equivalent to:
def my_view(request):
    if not request.user.is_superuser:
         return HttpResponse(status=403)  # HTTP 403 Forbidden 
'''


@user_passes_test(lambda u: u.is_superuser)
def myadmin(request):
    my_users = []
    for user in User.objects.raw('SELECT * FROM auth_user'):
        my_users.append({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'password': user.password,
            'is_superuser': user.is_superuser,
            'id': int(user.id)
        })
    return render(request, "myadmin.html", {"my_users": my_users})


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


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for encryption!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
