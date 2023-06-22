from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class CourseCreate(generics.CreateAPIView):
	permissions = [IsAuthenticated]
	queryset = Course.objects.all()
	serializer_class = CourseSerializer


class LessonCreate(generics.CreateAPIView):
	permissions = [IsAuthenticated]
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer


class LectureCreate(generics.CreateAPIView):
	permissions = [IsAuthenticated]
	queryset = Lecture.objects.all()
	serializer_class = LectureSerializer


class TaskCreate(generics.CreateAPIView):
	permissions = [IsAuthenticated]
	queryset = Task.objects.all()
	serializer_class = TaskSerializer


# class CourseDetails(generics.RetrieveUpdateAPIView):
# 	# permission_classes = [IsAuthenticated]
# 	queryset = Course.objects.all()
# 	serializer_class = CourseDetailsSerializer


class CourseList(generics.ListAPIView):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
	permission_classes = [IsAuthenticated]

class LessonRetrieveUpdateDetails(generics.RetrieveUpdateAPIView):
	# permission_classes = [IsAuthenticated]
	queryset = Lesson.objects.all()
	serializer_class = LessonSerializer


class CourseDetails(APIView):
	"""
	Retrieve, update or delete a snippet instance.
	"""
	def get_course(self, pk):
		try:
			return Course.objects.get(pk=pk)
		except Course.DoesNotExist:
			raise Http404


	def get_lessons(self, pk):
		try:
			return Lesson.objects.filter(course=pk)
		except Lesson.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		course = self.get_course(pk)
		lessons = self.get_lessons(pk)
		data = CourseDetailsSerializer(course).data

		# Сериализуем каждый объект Lesson
		lesson_serializer = LessonSerializer(lessons, many=True)
		lessons_data = lesson_serializer.data

		# Добавляем данные уроков к данным курса
		data['lessons'] = lessons_data
		return Response(data)


	def put(self, request, pk, format=None):
		course = self.get_course(pk)
		serializer = CourseDetailsSerializer(course, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		course = self.get_course(pk)
		course.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class LessonDetails(APIView):

	def get_lesson(self, pk):
		try:
			return Lesson.objects.get(pk=pk)
		except Lesson.DoesNotExist:
			raise Http404

	def get_lectures(self, pk):
		try:
			return Lecture.objects.filter(lesson=pk)
		except Course.DoesNotExist:
			raise Http404

	def get_tasks(self, pk):
		try:
			return Task.objects.filter(lesson=pk)
		except Course.DoesNotExist:
			raise Http404
	

	def get(self, request, pk, format=None):
		lesson 	 = self.get_lesson(pk)
		lectures = self.get_lectures(pk)
		tasks 	 = self.get_tasks(pk)

		data = LessonDetailsSerializer(lesson).data

		# Сериализуем каждый объект Lesson
		lecture_serializer = LectureSerializer(lectures, many=True)
		lecture_data = lecture_serializer.data

		# Сериализуем каждый объект Task
		task_serializer = TaskSerializer(tasks, many=True)
		tasks_data = task_serializer.data

		# Добавляем данные уроков к данным курса
		data['lectures'] = lecture_data
		data['tasks'] = tasks_data
		return Response(data)
