from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from backend_api.views import PostView, main_view
from django.conf import settings
from django.conf.urls.static import static
from contact.views import save_feedback

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', main_view, name ='main'),
    path('members/', include('members.urls')),
    path('api/feedback/', save_feedback),
    path('auth/', include('djoser.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)