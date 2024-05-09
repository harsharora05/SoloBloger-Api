from django.contrib import admin
from django.urls import path,include

from blog_app.api.views import CreateBlog,UpdateBlog
urlpatterns = [
path('create_blog/', CreateBlog.as_view(), name ="create-blog"),
path('update_blog/<int:pk>/', UpdateBlog.as_view(), name ="update-blog")
]