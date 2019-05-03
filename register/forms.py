from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    is_superuser = forms.BooleanField(initial=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    is_superuser = forms.BooleanField(label="Administrator")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'is_superuser']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'login_counter']


'''class MyAdminForm(forms.Form):
    first_name = forms.CharField(label='Firstname', max_length=100)
    last_name = forms.CharField(label='Lastname', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.PasswordInput(label='Reset Password', max_length=100)
    admin = forms.BooleanField(label='Is Admin', max_length=100)
'''