from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'password', 'email']


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')