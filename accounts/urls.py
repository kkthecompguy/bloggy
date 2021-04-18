from django.urls import path
from .views import register_view, login_view, profile_view
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
) 

# app_name = "accounts"
urlpatterns = [
  path('register/', register_view, name="register"),
  # path('login/', obtain_auth_token, name="login"),
  path('login/', login_view, name='login'),
  path('profile/', profile_view, name="profile"),
]