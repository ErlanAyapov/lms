from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class CourseCreate(generics.CreateAPIView):
	permissions = [IsAuthenticated]
	queryset = Course.objects.all()
	serializer_class = CourseCreateSerializer


class LessonCreate(generics.CreateAPIView):
	permissions = [IsAuthenticated]
	queryset = Lesson.objects.all()
	serializer_class = LessonCreateSerializer


class LectureCreate(generics.CreateAPIView):
	permissions = [IsAuthenticated]
	queryset = Lecture.objects.all()
	serializer_class = LectureCreateSerializer


class TaskCreate(generics.CreateAPIView):
	permissions = [IsAuthenticated]
	queryset = Task.objects.all()
	serializer_class = TaskCreateSerializer