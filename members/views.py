from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate, login, logout 
from .serializers import *
from rest_framework.request import Request
from rest_framework.response import Response  
from django.contrib.auth.hashers import make_password

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


@api_view(['POST'])
def login_view_api_view(request):
	serializer = LoginSerializer(data=request.data)  

	if serializer.is_valid():
		username = serializer.validated_data['username']
		password = serializer.validated_data['password'] 
		user = authenticate(request, username = username, password = password) 
		
		if user is not None:
			login(request, user)
			return Response(serializer.data, status = 201) 
	return Response({"message":"Данные не корректный!"}, status = 400)


@api_view(['POST'])
def logout_view_api_view(request):
	logout(request)
	return Response({'success': 'Выход из портала сделано!'})


@api_view(['POST'])
def user_customer_api_view(request):
	serializer = UserCustomerSerializer(data = request.data)

	if serializer.is_valid():
		serializer.save()
		return Response({'success': 'Регистрация завершена!'}, status = 201)
	else:
		return Response({"message":"Данные не корректный!"}, status = 400)

@api_view(['POST'])
def user_customer_create(request):  
	if request.method == 'POST':
		serializer = UserCustomerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response({"message":"Данные не корректный!"}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def user_customer_detail(request, pk): 
	try:
		user_customer = UserCustomer.objects.get(pk=pk)
		if request.method == 'GET':
			serializer = UserCustomerSerializer(user_customer)
			return Response(serializer.data)

		elif request.method == 'PUT': 
			serializer = UserCustomerSerializer(user_customer, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response({"message":"Данные не корректный!"}, status=400)

		elif request.method == 'DELETE':
			user_customer.delete()
			return Response({"message":"Данные удалены!"}, status=204)
	except UserCustomer.DoesNotExist:
		return Response({"message":"Данные не найдены!"}, status=404)


@api_view(['GET', 'PUT'])
def user_detail(request, pk):
	try:
		user = User.objects.get(pk=pk)
		if request.method == 'GET':
			serializer = UserDetailsSerializer(user)
			return Response(serializer.data)
		elif request.method == 'PUT': 
			serializer = UserUpdateSerializer(user, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response( UserDetailsSerializer(user).data )
			return Response({"message":"Данные не корректный!"}, status=400)

	except User.DoesNotExist:
		return Response({"message":"Данные не найдены!"}, status=404)