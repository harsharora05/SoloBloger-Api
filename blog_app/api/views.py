from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from blog_app.api.serializers import BlogSerializer,CommentSerializer
from blog_app.models import Blog,Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from blog_app.api.permissions import IsPostOwnerOrReadOnly,IsReviewOwnerOrReadOnly
from rest_framework import filters
from rest_framework import status
# Create your views here.


class CreateReview(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()
    
    def perform_create(self,serializer):
        pk = self.kwargs.get('pk')
        Selectedblog =  Blog.objects.get(id=pk)
        review_user = self.request.user
        serializer.save(blog=Selectedblog,ReviewUser = review_user)

class IncreaseLike(APIView):
    def post(self,request,pk):
        blg = Blog.objects.get(id=pk)
        blg.likes+=1
        blg.save()
        return Response({"message": "Like added.", "like_count": blg.likes}, status=status.HTTP_200_OK)
    

class DecreaseLike(APIView):
    def post(self,request,pk):
        blg = Blog.objects.get(id=pk)
        if(blg.likes > 0) :
            blg.likes-=1
            blg.save()
            return Response({"message": "Like removed.", "like_count": blg.likes}, status=status.HTTP_200_OK)
        else: 
            return Response({"message": "like can't be decreased any more."},status=status.HTTP_404_NOT_FOUND)

class ListReview(generics.ListAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        data = Comment.objects.filter(blog=pk)
        return data


class UpdateReview(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsReviewOwnerOrReadOnly]


class CreateBlog(APIView):
    permission_classes =[IsAuthenticatedOrReadOnly]
        
    def post(self,request):
        serializer= BlogSerializer(data = request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
            


class PopularBlog(generics.ListAPIView):
    queryset = Blog.objects.all().order_by("-likes")[:8]
    serializer_class = BlogSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

class RecentBlog(generics.ListAPIView):
    queryset = Blog.objects.all().order_by("-created")
    serializer_class = BlogSerializer
    pagination_class = PageNumberPagination
    permission_classes =  [IsAuthenticatedOrReadOnly]



class UpdateBlog(generics.RetrieveUpdateDestroyAPIView):
   queryset=Blog.objects.all()
   serializer_class =BlogSerializer
   permission_classes =[IsPostOwnerOrReadOnly]


class SearchBlog(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields =['title','category']