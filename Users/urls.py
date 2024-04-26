# urls.py
from django.urls import path
from .views import updateProfile, getProfile, getTravelists
from .views import RegisterAPIView, LoginAPIView, LogoutView


urlpatterns = [
    #/user/...
    path('register/', RegisterAPIView.as_view(), name='api_register'),
    path('login/', LoginAPIView.as_view(), name='api_login'),
    path('logout/', LogoutView.as_view(), name ='logout'),
    path('get_profile/', getProfile, name='get_profile'),
    path('update_profile/', updateProfile, name='update_profile'),
    path('user_travelists/', getTravelists, name='user_travelists'),
]
