from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from user.api.views import Register,logout,login

urlpatterns = [
    path('login/',login.as_view(),name ='Login'),
    path('register/',Register.as_view(),name ='Register'),
    path('logout/',logout.as_view(),name ='Logout'),
]
