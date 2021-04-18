from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Comment(models.Model):
  comment = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.comment


class Post(models.Model):
  # author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.CharField(max_length=255)
  comments = models.ManyToManyField(Comment, related_name='comments', blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.content