from django.contrib import admin
from django.urls import path,include

from blog_app.api.views import CreateBlog,UpdateBlog,CreateReview,ListReview,SearchBlog,UpdateReview,IncreaseLike,DecreaseLike
urlpatterns = [
path('create_blog/', CreateBlog.as_view(), name ="create-blog"),
path('increase_like/<int:pk>', IncreaseLike.as_view(), name ="increase-like"),
path('decrease_like/<int:pk>', DecreaseLike.as_view(), name ="decrease-like"),
path('update_blog/<int:pk>/', UpdateBlog.as_view(), name ="update-blog"),
path('search_blog/', SearchBlog.as_view(), name ="search-blog"),
path('review/<int:pk>/create/', CreateReview.as_view(), name ="create-review"),
path('review/<int:pk>/list/', ListReview.as_view(), name ="list-reviews"),
path('review/<int:pk>/', UpdateReview.as_view(), name ="list-detail"),
]