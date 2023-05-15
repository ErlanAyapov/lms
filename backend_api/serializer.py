from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'body']


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'date_joined']


class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'password', 'email']


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()