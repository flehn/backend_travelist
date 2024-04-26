
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

from Lists.serializer import ListSerializer
from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken 
'''
This data usually includes the user_id, but what if we wanted to include the username as well without having to make a separate request to the server?

To do this, we can create a custom serializer that extends the TokenObtainPairSerializer class and overrides the get_token() method. In this method, we can add a new claim to the token, such as the username. The modified serializer looks like this:
'''

'''
Login a user

required post request:
{
    "email": " ",
    "password": " "
}
'''
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    #https://stackoverflow.com/questions/54544978/customizing-jwt-response-from-django-rest-framework-simplejwt

    @classmethod
    def get_token(cls, user):

        token = RefreshToken.for_user(user)
        
        # Add custom claims
        token['username'] = user.username

        return token
    
    def validate(self, attrs):
        # Authenticate using email rather than username
        user = authenticate(email=attrs['email'], password=attrs['password'])
        
        if user is None:
            raise serializers.ValidationError('No user with this email and password was found.')

        data = super().validate(attrs)

        refresh = self.get_token(user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        #data['username'] = user.username  # Include the username in the response if desired

        return data

        

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class ProfileSerializer(serializers.ModelSerializer):
    notes = ListSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'