
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken 
'''
This data usually includes the user_id, but what if we wanted to include the username as well without having to make a separate request to the server?

To do this, we can create a custom serializer that extends the TokenObtainPairSerializer class and overrides the get_token() method. In this method, we can add a new claim to the token, such as the username. The modified serializer looks like this:
'''
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    #https://stackoverflow.com/questions/54544978/customizing-jwt-response-from-django-rest-framework-simplejwt

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)
    
    def validate(self, attrs):
        
        data = super().validate(attrs)

        refresh = self.get_token(self.user)
        

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        return data

        
    

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user