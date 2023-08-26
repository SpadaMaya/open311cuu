from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from open311cuu.SolicitudesOPEN311 import forms


from . import views

urlpatterns = [
    path('', views.Home, name='home'), 
    path('admin/', admin.site.urls),
    path('SolicitudesOPEN311', include("SolicitudesOPEN311.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register', views.register, name='register'),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
