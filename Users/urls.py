# urls.py
from django.urls import path
from .views import create_user, updateProfile, getProfile, getTravelists, CustomTokenObtainPairView


urlpatterns = [
    #/user/...
    path('create-user/', create_user, name='create_user'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login_user'),
    path('get_profile/', getProfile, name='get_profile'),
    path('update_profile/', updateProfile, name='update_profile'),
    path('user_travelists/', getTravelists, name='user_travelists'),
]
