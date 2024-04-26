from django.shortcuts import render

from django.contrib.auth import authenticate, login
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

from django.http import JsonResponse 
from rest_framework import generics, mixins, status

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework_simplejwt.views import TokenObtainPairView
from .user_serializer import *
from Lists.serializer import *
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAdminUser,
)

#Login User
"""
defines a custom token obtain view that uses a custom serializer 
for obtaining a JSON Web Token (JWT) pair for a user.
"""
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


#Create User 
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

"""
#Alternative:
#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
"""

#https://dev.to/ki3ani/implementing-jwt-authentication-and-user-profile-with-django-rest-api-part-3-3dh9

#/profile  and /profile/update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    print(f'request.user: {request.user}')
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTravelists(request):
    user_lists = TList.objects.filter(author=request.user)
    serializer = ListSerializer(user_lists, many=True)
    return Response(serializer.data)

