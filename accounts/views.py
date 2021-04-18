from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from .serializers import RegisterSerializer, UserSerializer
from .models import Account
from.decorators import is_authenticated
from django.http import HttpResponseBadRequest
import datetime, jwt

# Create your views here.

@api_view(['POST'])
def register_view(request):
  serializer = RegisterSerializer(data=request.data)
  data = {}

  if serializer.is_valid():
    user = serializer.save()
    data['status'] = status.HTTP_201_CREATED
    data['msg'] = 'Successfully registered a user'
    return Response(data, status=201)
  else:
    data = serializer.errors
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
  email = request.data.get('email')
  password = request.data.get('password')

  user = Account.objects.filter(email=email).first()

  if user is None:
    raise AuthenticationFailed("Invalid credentials")

  if not user.check_password(password):
    raise AuthenticationFailed("Invalid credentials")
    
  payload = {
    'id': user.id,
    'email': user.email,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
    'iat': datetime.datetime.utcnow()
  }

  token = jwt.encode(payload, 'jwtSecret', algorithm='HS256')

  response = Response()
  response.set_cookie(key="jwt", value=token, httponly=True)
  response.data = {
    'token': token,
    'id': user.id,
    'email': user.email,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
    'iat': datetime.datetime.utcnow()
  }

  return response


@api_view(['GET'])
@is_authenticated
def profile_view(request):
  user = get_object_or_404(Account, pk=request.user.id)
  response = {
    'id': user.id,
    'username': user.username,
    'email': user.email
  }

  return Response(response)