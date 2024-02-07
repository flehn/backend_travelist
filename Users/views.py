from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse 
from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework_simplejwt.views import TokenObtainPairView
from .user_serializer import CustomTokenObtainPairSerializer
from .user_serializer import UserSerializer


#Login User
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


'''
https://dev.to/ki3ani/implementing-jwt-authentication-and-user-profile-with-django-rest-api-part-3-3dh9

#api/profile  and api/profile/update
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
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

#api/notes
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    public_notes = Note.objects.filter(is_public=True).order_by('-updated')[:10]
    user_notes = request.user.notes.all().order_by('-updated')[:10]
    notes = public_notes | user_notes
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


'''