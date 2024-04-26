from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

from Lists.serializer import ListSerializer

User = get_user_model()


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = RefreshToken.for_user(user)
        # Add custom claims
        token['username'] = user.get_username()  # Assuming you're using the email as the username field
        return token
    
    def validate(self, attrs):
        # Authenticate using email and password
        user = authenticate(email=attrs.get('email'), password=attrs.get('password'))
        if user is None:
            raise serializers.ValidationError('No user with this email and password was found.')

        data = super().validate(attrs)
        refresh = self.get_token(user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        # Optionally include the username (or email) in the response
        # data['username'] = user.get_username()

        return data

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



class ProfileSerializer(serializers.ModelSerializer):
    # Assuming 'tlists' is the related name for TList instances associated with this user
    tlists = ListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'tlists']  # Include relevant fields and the related travel lists


