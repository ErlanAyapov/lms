from django.urls import path
from django.urls import re_path as url
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('create/', CourseCreate.as_view()),
    path('lesson-create/', LessonCreate.as_view()),
    path('lecture-create/', LectureCreate.as_view()),
    path('task-create/', TaskCreate.as_view()),
    path('<int:pk>/', CourseDetails.as_view()),
    path('', CourseList.as_view()),
    path('lesson-retrieve-update/<int:pk>', LessonRetrieveUpdateDetails.as_view()),
    path('lesson/<int:pk>', LessonDetails.as_view())
]