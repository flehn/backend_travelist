# views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .user_serializer import ProfileSerializer, UserRegisterSerializer
from Lists.serializer import ListSerializer
import os

from Lists.models import TList
from django.shortcuts import get_object_or_404

ENV_ROLE = os.getenv('DJANGO_ENV_ROLE', 'development')
if ENV_ROLE == 'production':
    secure_boolean = True
    #samesite_var = 'None'
else:
    secure_boolean = False
    #samesite_var = 'Lax'


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
Token Based Authentification:
For clients to authenticate, the token key should be included in the Authorization HTTP header. 
The key should be prefixed by the string literal "Token", 
with whitespace separating the two strings. For example:
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
'''

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)  # Generate token for the user
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Login successful'
            }, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
          try:
               refresh_token = request.data["refresh_token"]
               token = RefreshToken(refresh_token)
               token.blacklist()
               return Response(status=status.HTTP_205_RESET_CONTENT)
          except Exception as e:
               return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    # Fetch the requesting user's profile
    user = request.user
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        # Return an error response if the data is not valid
        return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTravelists(request):
    # Fetch all travel lists created by the requesting user
    user_lists = TList.objects.filter(author=request.user)
    serializer = ListSerializer(user_lists, many=True)
    return Response(serializer.data)