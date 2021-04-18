from .test_setup import TestSetUp

class TestViews(TestSetUp):
  def test_user_cannot_register_with_nodata(self):
    res = self.client.post(self.register_url) 
    self.assertEqual(res.status_code, 400)

  def test_user_can_register_correctly(self):
    res = self.client.post(self.register_url, self.user_data, format="json") 
    self.assertEqual(res.status_code, 201)
  
  def test_user_cannot_login_without_data(self):
    res = self.client.post(self.login_url)
    self.assertEqual(res.status_code, 403)

  def test_user_can_login_correctly(self):
    res = self.client.post(self.register_url, self.user_data, format="json") 
    self.assertEqual(res.status_code, 201)

    res = self.client.post(self.login_url, self.user_data, format="json")
    self.assertEqual(res.status_code, 200)

  def test_user_cannot_create_posts_unauthorized(self):
    res = self.client.post(self.post_create_url, self.post_data, format="json")
    self.assertEqual(res.status_code, 403)

  def test_user_can_create_posts_after_login(self):
    resp = self.client.post(self.register_url, self.user_data, format="json") 
    self.assertEqual(resp.status_code, 201)

    response = self.client.post(self.login_url, self.user_data, format="json")
    self.assertEqual(response.status_code, 200) 

    res = self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    res = self.client.post(self.post_create_url, self.post_data, format="json") 
    self.assertEqual(res.status_code, 201)  


  def test_user_cannot_list_posts_unauthenticated(self):
    response = self.client.get(self.post_list_url)
    self.assertEqual(response.status_code, 403) 
  
  def test_user_can_list_posts__after_login(self):
    resp = self.client.post(self.register_url, self.user_data, format="json") 
    self.assertEqual(resp.status_code, 201)

    response = self.client.post(self.login_url, self.user_data, format="json")
    self.assertEqual(response.status_code, 200) 

    res = self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    res = self.client.get(self.post_list_url) 
    self.assertEqual(res.status_code, 200) 

  def test_user_cannot_view_post_detail_unauthenticated(self):
    response = self.client.get(self.post_detail_url)
    self.assertEqual(response.status_code, 403)

  def test_user_can_view_post_detail_after_login(self):
    resp = self.client.post(self.register_url, self.user_data, format="json") 
    self.assertEqual(resp.status_code, 201)

    response = self.client.post(self.login_url, self.user_data, format="json")
    self.assertEqual(response.status_code, 200) 

    res = self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    res = self.client.post(self.post_create_url, self.post_data, format="json") 
    self.assertEqual(res.status_code, 201)

    res = self.client.get(self.post_detail_url) 
    self.assertEqual(res.status_code, 200) 

  def test_user_cannot_comment_on_post_unauthenticated(self):
    response = self.client.post(self.post_comment_url)
    self.assertEqual(response.status_code, 403)

  def test_user_can_comment_on_post_after_login(self):
    resp = self.client.post(self.register_url, self.user_data, format="json") 
    self.assertEqual(resp.status_code, 201)

    response = self.client.post(self.login_url, self.user_data, format="json")
    self.assertEqual(response.status_code, 200) 

    res = self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    res = self.client.post(self.post_create_url, self.post_data, format="json") 
    self.assertEqual(res.status_code, 201)

    res = self.client.post(self.post_comment_url, self.comment_data, format="json") 
    self.assertEqual(res.status_code, 201)

  def test_user_can_update_post_after_login(self):
    resp = self.client.post(self.register_url, self.user_data, format="json") 
    self.assertEqual(resp.status_code, 201)

    response = self.client.post(self.login_url, self.user_data, format="json")
    self.assertEqual(response.status_code, 200) 

    res = self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    res = self.client.post(self.post_create_url, self.post_data, format="json") 
    self.assertEqual(res.status_code, 201)

    res = self.client.put(self.post_update_url, self.comment_data, format="json") 
    self.assertEqual(res.status_code, 200)

  def test_user_can_delete_post_after_login(self):
    resp = self.client.post(self.register_url, self.user_data, format="json") 
    self.assertEqual(resp.status_code, 201)

    response = self.client.post(self.login_url, self.user_data, format="json")
    self.assertEqual(response.status_code, 200) 

    res = self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    res = self.client.post(self.post_create_url, self.post_data, format="json") 
    self.assertEqual(res.status_code, 201)

    res = self.client.delete(self.post_delete_url) 
    self.assertEqual(res.status_code, 200)
  