from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from user.api.views import Register,logout

urlpatterns = [
    path('login/',obtain_auth_token,name ='Login'),
    path('register/',Register.as_view(),name ='Register'),
    path('logout/',logout.as_view(),name ='Logout'),
]
