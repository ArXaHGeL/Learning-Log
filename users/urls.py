"""Defines URL patterns for users."""
from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    # Login page
    path('', include('django.contrib.auth.urls')),
    # Logout page
    path('logout/', views.logout_view, name='logout'),
    # Registration page
    path('register/', views.register, name='register'),
]
