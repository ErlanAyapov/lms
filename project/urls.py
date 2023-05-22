from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from backend_api.views import PostView, main_view
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/', PostView.as_view(), name='post'), 
    path('', main_view, name ='main'),
    path('members/', include('members.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
Регистрация 
members/api/register

Авторизация
members/api/auth

Выход
members/api/logout
'''