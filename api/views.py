from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'Users': {
      'Login': '/api/v1/users/login',
      'Register': '/api/v1/users/register'
    },
    'Posts': {
      'Create': '/api/v1/posts/create',
      'Detail': '/api/v1/posts/detail/<str:pk>',
      'List': '/api/v1/posts/list',
      'Comment': '/api/v1/posts/comment/<str:pk>',
      'Update': '/api/v1/posts/update/<str:pk>',
      'Delete': '/api/v1/posts/delete/<str:pk>',
      'List Comments': '/api/v1/posts/comments'
    }
  }
  return Response(api_urls) 