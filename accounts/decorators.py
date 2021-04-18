from rest_framework.exceptions import AuthenticationFailed
from .models import Account
import jwt

def is_authenticated(view_func):
  def wrapper_func(request, *args, **kwargs):
    token = request.META.get('HTTP_AUTHORIZATION')

    if not token:
      raise AuthenticationFailed('Unauthorized')

    tokenOnly = token.split(" ")[1]
  
    try:
      decoded = jwt.decode(tokenOnly, 'jwtSecret', algorithms=['HS256'])

      user = Account.objects.filter(id=decoded['id']).first()

      request.user = user

      return view_func(request, *args, **kwargs)
    except jwt.ExpiredSignatureError:
      raise AuthenticationFailed("Unauthorized")
    except jwt.InvalidSignatureError:
      raise AuthenticationFailed("Unauthorized")
  return wrapper_func
  
  

  