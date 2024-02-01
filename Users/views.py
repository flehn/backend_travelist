from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .user_serializer import UserSerializer
from django.contrib.auth import authenticate, login

#Create User 
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


#Login User 
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        # One can add logic to create and send a token/session ID here for debugging
        return Response({'message': 'Login successful'})
    else:
        return Response({'error': 'Invalid credentials'}, status=401)