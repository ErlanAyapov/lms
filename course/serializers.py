from rest_framework import serializers
from .models import * 
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name')


class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('__all__')


class LessonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = ('course', 'start_time', 'end_time', 'title')


class LectureSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lecture
		fields = ('__all__')


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('__all__')


class CourseDetailsSerializer(serializers.ModelSerializer):
	lessons  = LessonSerializer(many = True, read_only = True)
	teachers = UserSerializer(many = True, read_only = True)
	students = UserSerializer(many = True, read_only = True)

	class Meta:
		model = Course
		fields = ('id', 'teachers', 'students', 'title', 'description', 'start_time', 'end_time', 'price', 'lessons')
		read_only_fields = fields