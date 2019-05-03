from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    is_superuser = forms.BooleanField(initial=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class PasswordReset(UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=True)
    is_superuser = forms.BooleanField(label="Administrator", required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'is_superuser']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'login_counter']
