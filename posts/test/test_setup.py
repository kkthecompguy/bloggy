from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
  def setUp(self):
    self.register_url = reverse("register")
    self.login_url = reverse("login")
    self.post_create_url = reverse("create")
    self.post_list_url = reverse("list_posts")
    self.post_detail_url = reverse("detail", kwargs={'pk':1})
    self.post_comment_url = reverse("comment", kwargs={'pk': 1}) 
    self.post_update_url = reverse("update", kwargs={'pk': 1})
    self.post_delete_url = reverse("delete", kwargs={'pk': 1})

    self.user_data = {
      "email": "newuser@gmail.com",
      "username": "newuser",
      "password": "password@123"
    }

    self.access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NCwiZW1haWwiOiJuZXd1c2VyQGdtYWlsLmNvbSIsImV4cCI6MTYxODczMzIzNCwiaWF0IjoxNjE4NzI5NjM0fQ.ObSIf6kF-xaQbDKIva9aFM9CVQlWTfV1Hl9cRVsESNE"

    self.post_data = {
      "content": "new post created for test"
    }

    self.comment_data = {
      "comment": "New comment"
    }

    return super().setUp()

  def tearDown(self):
    return super().tearDown()