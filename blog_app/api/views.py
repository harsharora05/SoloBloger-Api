from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework import generics
from blog_app.api.serializers import BlogSerializer
from blog_app.models import Blog
# Create your views here.



class CreateBlog (APIView):
    def get(self,request):
        data = Blog.objects.all()
        serializer = BlogSerializer(data,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        serializer= BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)



class UpdateBlog(generics.RetrieveUpdateDestroyAPIView):
   queryset=Blog.objects.all()
   serializer_class =BlogSerializer

