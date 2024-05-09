from django.shortcuts import render
from django.contrib.auth.models import User
from  rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from user.api.serializers import UserSerializer
from rest_framework.response import Response
# Create your views here.

class logout(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response({"message" : "logut sucessfull"})

class Register(APIView):
    
    def post(self,request):
        AuthData = request.data
        serializer = UserSerializer(data = AuthData)
        data ={}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'registeration successfull',
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.create(user = account)
            data['token'] = str(token)
        else:
            data = serializer.errors
        return Response(data)
