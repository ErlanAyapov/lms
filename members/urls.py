from django.urls import path
from django.urls import re_path as url
from .views import *



urlpatterns = [
    path('api/register/', register_view, name='register'),
    path('api/auth/', login_view, name='auth'),
    path('api/logout/', logout_view, name='logout'),
    path('api/register-finish/', user_customer, name = 'register-finish'),
    path('api/profile/', ProfileDetailAPIView.as_view(), name='profile-detail'),
    
]