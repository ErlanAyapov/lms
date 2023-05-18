from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserCustomer


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


class UserCustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserCustomer
		fields = ('user', 'image', 'phone_number', 'user_role', 'birth_day', 'biography', 'user_ip', 'address', 'mail_index')



class UserDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'