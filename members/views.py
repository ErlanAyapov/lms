from django.shortcuts import render
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model 
from django.contrib.auth import authenticate, login, logout 
from .serializer import *
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics 
from rest_framework.views import APIView 
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser  


User = get_user_model()


# Create your views here.
@api_view()
def user(request: Request):
	return Response({
		'data': UserSerializer(request.user).data
	})


@api_view(['POST'])
def register_view_api_view(request):
	serializer = UserSerializer(data=request.data)

	if serializer.is_valid():
		user = serializer.save()
		login(request, user)
		return Response(serializer.data, status=201)
	else:
		return Response(serializer.errors, status=400)


@api_view(['POST'])
def login_view_api_view(request):
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
		return Response(serializer.errors, status = 400)

@api_view(['POST'])
def user_customer_create(request):  
	if request.method == 'POST':
		serializer = UserCustomerSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_customer_detail(request, pk): 
	try:
		snippet = UserCustomer.objects.get(pk=pk)
		if request.method == 'GET':
			serializer = UserCustomerSerializer(snippet)
			return Response(serializer.data)

		elif request.method == 'PUT': 
			serializer = UserCustomerSerializer(snippet, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=400)

		elif request.method == 'DELETE':
			snippet.delete()
			return HttpResponse(status=204)
	except UserCustomer.DoesNotExist:
		return Response(status=404)




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
			return Response(serializer.errors, status=400)

	except User.DoesNotExist:
		return Response(status=404)