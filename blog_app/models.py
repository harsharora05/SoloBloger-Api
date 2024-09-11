from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Post_Owner')
    title = models.CharField(max_length=50 ,blank=False,null=False)
    content = models.CharField(max_length=1500 ,blank=False,null=False)
    img = models.ImageField(upload_to='blog/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title + " | " + self.user.username
    


class Comment(models.Model):
    ReviewUser = models.ForeignKey(User,on_delete=models.CASCADE,related_name="review_user")
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    desc = models.CharField(max_length=300)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.ReviewUser.username + " | " + self.blog.title