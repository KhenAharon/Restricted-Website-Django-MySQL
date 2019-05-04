from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from .models import User
from django.contrib.auth.decorators import user_passes_test
import mysql.connector

# a non-django, general python mysql-connector
mydb = mysql.connector.connect(
  host="localhost",
  user="khen",
  database="mydb",
  passwd="khen"
)
mycursor = mydb.cursor()


def login_success(request):
    """
    when logging in, the login is counted, so we can recognize a first login and offer to reset password.
    :param request: the client http request that includes user info.
    :return: redirect page
    """
    if request.user.profile.login_counter == 0:
        request.user.profile.login_counter += 1
        request.user.save()  # save to db.
        return redirect("change_password")
    else:
        return redirect("home")


def home(request):
    """
    Homepage view
    :param request: the client request
    :return: rendering homepage with info about wether this is first user login
    """
    if request.user.is_authenticated:  # is the user logged in
        context = {
            'users': User.objects.all().first(),
            'login_count': User.objects.filter(username=request.user).first().profile.login_counter
        }
    else:
        context = {
            'users': User.objects.all().first(),
            'login_count': 'unsigned'  # if the user is not connected then we don't send a number.
        }
    return render(request, "home.html", context)


@user_passes_test(lambda u: u.is_superuser)
def edit_user2(request, id=0):
    """
    This function is an old Django-based model function that is not used, but works. look at edit_user
    """
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
    """
    Resetting a password is permitted only for admin.
    Also the admin know only the SHA256 pass because it's a one-way function, therefore can only reset.

    The decorator above with the lambda expression is equivalent to:
    def my_view(request):
    if not request.user.is_superuser:
         return HttpResponse(status=403)  # HTTP 403 Forbidden
    Namely, function is performed only if the user is admin.

    :param request: client http request.
    :param id: user id in the database.
    :return: a redirect page after resetting the password.
    """
    user_to_update = User.objects.raw('SELECT * FROM auth_user WHERE id=' + str(id))
    user_to_update = user_to_update[0]  # there is only one such id, the user is in first index.

    if request.method == 'POST':  # if the user sent a post request to reset the pass via the form.
        form = SetPasswordForm(user_to_update, request.POST)  # reset password form, without entering old pass.
        if form.is_valid():
            form.save()  # saving to the db.
            messages.success(request, 'The password was reset!')
            return redirect('myadmin')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SetPasswordForm(user=user_to_update)
    return render(request, 'reset_password.html', {'p_form': form})


@user_passes_test(lambda u: u.is_superuser)
def edit_user(request, id=0):
    """
    Editing a user by admin only.
    Includes raw sql commands for an example of this usage, without using the django ORM (abbreviated way for the sql).
    :param request: http request by admin.
    :param id: id of the user to edit.
    :return: a redirect to the main users to edit page.
    """
    user_to_update = User.objects.raw('SELECT * FROM auth_user WHERE id=' + str(id))  # select a user with this id
    user_to_update = user_to_update[0]  # there is only one such id, the user is in first index.

    if request.method == 'POST':  # if the admin posted a request to change the user
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

            # SQL update command
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

    # transferring the id of the user to the context if reset password is clicked in the page.
    context = {
        "id": id,
        'u_form': u_form
    }

    return render(request, "edituser.html", context)


@user_passes_test(lambda u: u.is_superuser)
def myadmin(request):
    """
    MyAdmin page that is equivalent to the Django default admin page.
    more example for raw sql.
    :param request: the http request to myadmin page.
    :return: myadmin page.
    """
    my_users = []
    for user in User.objects.raw('SELECT * FROM auth_user'):  # select all columns of the user, for all users
        my_users.append({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'password': user.password,
            'is_superuser': user.is_superuser,
            'id': int(user.id)
        })  # adding the user to the db.
    return render(request, "myadmin.html", {"my_users": my_users})


def register(request):
    """
    Register page.
    :param request: http request.
    :return: register page.
    """
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
    """
    Profile page with all user attributes to change.
    :param request: http request.
    :return: the profile page with fields autofilling.
    """
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
    """
    Change password page.
    :param request: http request.
    :return: change password page.
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Updating a user's password logs out all sessions for the user.
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
