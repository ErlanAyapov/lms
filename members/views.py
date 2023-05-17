from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate, login, logout 
from .serializer import UserRegisterSerializer, UserSerializer, LoginSerializer, UserCustomerSerializer
from rest_framework.request import Request
from rest_framework.response import Response



User = get_user_model()


# Create your views here.
@api_view()
def user(request: Request):
	return Response({
		'data': UserSerializer(request.user).data
	})


@api_view(['POST'])
def register_view(request):
	serializer = UserSerializer(data=request.data)

	if serializer.is_valid():
		user = serializer.save()
		login(request, user)
		return Response(serializer.data, status=201)
	else:
		return Response(serializer.errors, status=400)


@api_view(['POST'])
def login_view(request):
	serializer = LoginSerializer(data=request.data)

	if serializer.is_valid():
		username = serializer.validated_data['username']
		password = serializer.validated_data['password']

		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return Response({'success': 'Авторизация пройдена!'}, status = 201)
		else:
			return Response({'error': 'Неверный имя пользователя или пороль!'}, status = 400)
	else:
		return Response(serializer.errors, status = 400)


@api_view(['POST'])
def logout_view(request):
	logout(request)
	return Response({'success': 'Выход из портала сделано!'})


@api_view(['POST'])
def user_customer(request):
	serializer = UserCustomerSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()
		return Response({'success': 'Регистрация завершена!'}, status = 201)
	else:
		return Response(serializer.errors, status = 400)