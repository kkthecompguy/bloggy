from django.urls import path, include
from .views import apiOverview

# app_name = "api"
urlpatterns = [
  path('', apiOverview, name="index"),
  path('posts/', include('posts.urls')),
  path('users/', include('accounts.urls')),
]
