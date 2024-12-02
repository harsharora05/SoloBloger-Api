from rest_framework import serializers
from blog_app.models import Blog,Comment,BlogImage

class CommentSerializer(serializers.ModelSerializer):
    blog = serializers.StringRelatedField(read_only = True)
    ReviewUser = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Comment
        fields ="__all__"




class BlogSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    Blog_Images= serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Blog
        fields = "__all__"
    


