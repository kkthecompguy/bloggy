from django.urls import path
from .views import create, list_posts, comment, detail, delete, update, list_comments

# app_name="posts"
urlpatterns = [
  path('create/', create, name="create"),
  path('detail/<str:pk>', detail, name="detail"),
  path('list/', list_posts, name="list_posts"),
  path('update/<str:pk>', update, name="update"),
  path('comment/<str:pk>', comment, name="comment"),
  path('delete/<str:pk>', delete, name="delete"),
  path('comments/', list_comments, name="list_comments"),
]
