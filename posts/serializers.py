from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework import permissions
from .models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'password', 'email']


class PostCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ['content']


class PostListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ['id', 'content', 'comments', 'created_at', 'update_at']


class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['comment']

class CommentListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = [ 'id', 'comment', 'created_at']