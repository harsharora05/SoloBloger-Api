from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    categories=(
        ("SPORTS" ,"Sports"),
        ("BUSINESS" , "Business"),
        ("ENTERTAINMENT" , "Entertainment"),
        ("LIFE" , "Life"),
        ("FOOD" , "Food")
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='Post_Owner')
    title = models.CharField(max_length=50 ,blank=False,null=False)
    category = models.CharField(max_length=100,blank=False,null=False,choices=categories)
    content = models.TextField(max_length=4000,blank=False,null=False)
    img = models.ImageField(upload_to='blog/')
    likes = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title + " | " + self.user.username
    




class Comment(models.Model):
    ReviewUser = models.ForeignKey(User,on_delete=models.CASCADE,related_name="review_user")
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    desc = models.CharField(max_length=1700)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.ReviewUser.username + " | " + self.blog.title