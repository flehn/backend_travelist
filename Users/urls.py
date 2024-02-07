# urls.py
from django.urls import path
from .views import create_user, CustomTokenObtainPairView


urlpatterns = [
    #/user/...
    path('create-user/', create_user, name='create_user'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login_user'),
]
