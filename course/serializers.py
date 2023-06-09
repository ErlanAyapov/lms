from rest_framework import serializers
from .models import *


class CourseCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Course
		fields = ('__all__')


class LessonCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lesson
		fields = ('__all__')


class LectureCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Lecture
		fields = ('__all__')


class TaskCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('__all__')