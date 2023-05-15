from django.urls import path
from django.urls import re_path as url
from .views import user, register_view, login_view, logout_view



urlpatterns = [
    path('api/register/', register_view, name='register'),
    path('api/auth/', login_view, name='auth'),
    path('api/logout/', logout_view, name='logout'),
]