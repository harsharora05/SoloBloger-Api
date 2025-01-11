from django.shortcuts import render
from django.contrib.auth.models import User
from  rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from user.api.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
# Create your views here.

class logout(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response({"message" : "logut sucessfull"},status= status.HTTP_200_OK)

class login(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response(
                {"message": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)

        if user is not None:
            token,created = Token.objects.get_or_create(user = user)
            return Response({"message" : "Login SuccessFull","username":username,"email":user.email,"token":token.key},status=status.HTTP_200_OK)
        else:
            return Response({"message" : "Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)






class Register(APIView):
    
    def post(self,request):
        AuthData = request.data
        serializer = UserSerializer(data = AuthData)
        data ={}
        if serializer.is_valid():
            account = serializer.save()
            data['message'] = 'Registeration Successfull',
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.create(user = account)
            data['token'] = str(token)
            return Response(data,status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data,status=status.HTTP_401_UNAUTHORIZED)
        
