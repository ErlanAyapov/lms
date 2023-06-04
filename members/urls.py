from django.urls import path
from django.urls import re_path as url
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('api/register/', register_view_api_view, name='register'), 
    path('api/user/', UserDetail.as_view(), name='profile'),
    path('api/user-customer/<int:pk>/', UserCustomerDetail.as_view(), name='user-customer'),
    path('api/user-customer-create/', UserCustomerCreate.as_view(), name='user-customer-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]