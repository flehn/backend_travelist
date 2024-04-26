# forms.py

'''
Create forms for user registration and authentication.
'''
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('email', 'password')
