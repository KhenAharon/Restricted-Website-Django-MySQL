from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # fields for the registration form.
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    is_superuser = forms.BooleanField(initial=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class PasswordReset(UserCreationForm):
    # fields for password reset form.
    class Meta:
        model = User
        fields = ['password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    # fields for user editing by the admin.
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=True)
    is_superuser = forms.BooleanField(label="Administrator", required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'is_superuser']


class ProfileUpdateForm(forms.ModelForm):
    # fields of profile update form.
    class Meta:
        model = Profile
        fields = ['image', 'login_counter']
