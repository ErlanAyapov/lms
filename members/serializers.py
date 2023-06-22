from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserCustomer
from course.models import Course
from course.serializers import CourseSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')


class UserUpdateSerializer(serializers.ModelSerializer): 
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'email')


class UserCustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserCustomer
		fields = ('__all__') 


class UserDetailsSerializer(serializers.ModelSerializer):
	usercustomer = UserCustomerSerializer()
	courses = serializers.SerializerMethodField()

	def get_courses(self, user):
		if user.is_staff:
			courses = Course.objects.all()
		else:
			courses = Course.objects.filter(teacher=user)  
		return CourseSerializer(courses, many=True).data

	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'email', 'usercustomer', 'courses')
