from django.shortcuts import render, get_object_or_404 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import PostCreateSerializer, PostListSerializer, CommentSerializer, CommentListSerializer
from .models import Post, Comment
from accounts.decorators import is_authenticated
from rest_framework.pagination import PageNumberPagination

# Create your views here.


@api_view(['POST'])
@is_authenticated
def create(request):
  serializer = PostCreateSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()

  return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@is_authenticated
def list_posts(request):
  posts = Post.objects.all().order_by('-created_at')
  paginator = PageNumberPagination()
  paginator.page_size = 10
  post_objects = posts
  result_page = paginator.paginate_queryset(post_objects, request)
  serializer = PostListSerializer(result_page, many=True)
  return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@is_authenticated
def detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  serializer = PostListSerializer(post, many=False)
  return Response(serializer.data)

  
@api_view(['POST'])
@is_authenticated
def comment(request, pk):
  post = get_object_or_404(Post, pk=pk)
  serializer = CommentSerializer(data=request.data)
  if serializer.is_valid():
    comment = serializer.save()
    post.comments.add(comment)
    post.save()
    return Response({'msg': 'Comment added successfully'}, status=status.HTTP_201_CREATED)
  else:
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@is_authenticated
def update(request, pk):
  post = get_object_or_404(Post, pk=pk)
  serializer = PostCreateSerializer(instance=post, data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response({'msg': 'Post Updated Successfully'})
  else:
    return Response(serializer.errors)

  

@api_view(['DELETE'])
@is_authenticated
def delete(request, pk):
  post = get_object_or_404(Post, pk=pk)
  post.delete()
  return Response({ 'msg': 'Post deleted successfully' })


@api_view(['GET'])
@is_authenticated
def list_comments(request):
  comments = Comment.objects.all().order_by('-created_at')
  paginator = PageNumberPagination()
  paginator.page_size = 10
  post_objects = comments
  result_page = paginator.paginate_queryset(post_objects, request)
  serializer = CommentListSerializer(comments, many=True)
  return paginator.get_paginated_response(serializer.data)
