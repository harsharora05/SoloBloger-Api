from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=50 ,blank=False,null=False)
    content = models.CharField(max_length=200 ,blank=False,null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

