from django.db import models
from django import forms
from django.contrib.auth.models import User



class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')
       

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
# Create your models here.

class Comment(models.Model):
    objects = models.Manager()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    
    created_at = models.DateTimeField(auto_now_add=True)
