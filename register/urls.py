from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


#  These are url paths for the view functions.
urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.home, name='welcome'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('login-success/', views.login_success, name='login_success'),
    path('myadmin/', views.myadmin, name='myadmin'),
    path('edit-user/<int:id>/', views.edit_user, name='edit_user'),
    path('password-reset/<int:id>/', views.password_reset, name='password_reset'),
]
