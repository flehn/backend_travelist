"""Travellist_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Auth.views import LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("lists/", include("Lists.urls")),
    #path("users/", include("Users.urls")),

    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/logout/", LogoutView.as_view()),
]

'''
Below are the Djoser URLs we'll be utilizing:

/users/: Submitting a POST request to this route creates a new user account on the Django backend, serving as the registration process.
/users/me/: A GET request to this endpoint returns information about the currently authenticated user, requiring the user to be logged in.
/users/reset_password/: A POST request here initiates a password reset process by sending an email to the provided address with a password reset link, but only if the user account exists.
/users/reset_password_confirm/: By making a POST request to this route with the uid, token, and new_password, the user can reset their password to the new value specified in the new_password field.
/jwt/create/: This endpoint is used for logging in, where it authenticates the user and returns a JWT for subsequent authenticated requests.
/jwt/refresh/: This endpoint is for refreshing an existing access token by providing a valid refresh token, thus granting a new access token.
'''

