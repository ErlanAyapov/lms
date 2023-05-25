from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate, login, logout 
from .serializers import *
from rest_framework.request import Request
from rest_framework.response import Response  
from django.contrib.auth.hashers import make_password
from rest_framework import generics



User = get_user_model()


@api_view(['POST'])
def register_view_api_view(request):
	serializer = UserRegisterSerializer(data=request.data)
	
	if serializer.is_valid():
		password = serializer.validated_data['password']
		hashed_password = make_password(password)  # Хэширование пароля
		serializer.validated_data['password'] = hashed_password
		serializer.save()
		return Response(serializer.data, status=201) 
	return Response({"message": "Данные не корректные!"}, status=400)


class UserCreate(generics.GenericAPIView):
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializer

	def post(self, request, *args, **kwargs):
		# print(self)
		return self.create(request, *args, **kwargs)


class UserCustomerCreate(generics.CreateAPIView):
	queryset = UserCustomer.objects.all()
	serializer_class = UserCustomerSerializer


class UserCustomerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = UserCustomer.objects.all()
	serializer_class = UserCustomerSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserDetailsSerializer