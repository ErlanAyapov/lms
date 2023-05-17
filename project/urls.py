from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from backend_api.views import PostView, main_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/', PostView.as_view(), name='post'), 
    path('', main_view, name ='main'),
    path('members/', include('members.urls'))
]

'''
Регистрация 
members/api/register

Авторизация
members/api/auth

Выход
members/api/logout
'''