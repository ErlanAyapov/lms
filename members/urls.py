from django.urls import path
from django.urls import re_path as url
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('api/register/', register_view_api_view, name='register'),
    path('api/auth/', login_view_api_view, name='auth'),
    path('api/logout/', logout_view_api_view, name='logout'),
    path('api/register-finish/', user_customer_api_view, name = 'register-finish'),
    path('api/user/<int:pk>/', user_detail, name='profile'),
    path('api/user-customer/<int:pk>/', user_customer_detail, name='profile-detail'),
    path('api/user-customer-create/', user_customer_create, name='user-customer-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]