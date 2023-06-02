from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate, login, logout 
from .serializers import *
from rest_framework.request import Request
from rest_framework.response import Response  
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


User = get_user_model()


@api_view(['POST'])
def register_view_api_view(request):
	serializer = UserRegisterSerializer(data=request.data)
	
	if serializer.is_valid():
		password = serializer.validated_data['password']
		hashed_password = make_password(password)
		serializer.validated_data['password'] = hashed_password
		serializer.save()
		return Response(serializer.data, status=201) 
	return Response({"message": "Данные не корректные!"}, status=400)


class UserCustomerCreate(generics.CreateAPIView):
	permission_classes = [IsAuthenticated]
	queryset = UserCustomer.objects.all()
	serializer_class = UserCustomerSerializer


class UserCustomerDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = UserCustomer.objects.all()
	serializer_class = UserCustomerSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAuthenticatedOrReadOnly]
	queryset = User.objects.all()
	serializer_class = UserDetailsSerializer