### Blog Post API Technical Assessment 
This is the blog post build on djangoresetframework

### Setup/Installation Requirements
Ensure you have python installed on your machine.
If you are using linux Os, you need to install pip3 ```sudo apt-get install python3-pip```

Activate a virtualenv ---- best pratice ---- ```virtualenv venv && source venv/bin/activate```

Install Django & DjangoRestFramework & Project dependencies ```pip3 install -r requirements.txt```

Make migrations & Run the server ```python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver```

Use postman or any other rest client for testing

### API Endpoints
Authentication
``` /api/v1/users/register ```
``` /api/v1/users/login ```

Posts
``` /api/v1/posts/create```
``` /api/v1/posts/detail/<str:pk>```
``` /api/v1/posts/list```
``` /api/v1/posts/comment/<str:pk>```
``` /api/v1/posts/update/<str:pk>```
``` /api/v1/posts/delete/<str:pk>```
``` /api/v1/posts/comments ```

### Unit Testing 
For unit testing there are 14 tests which the api must pass ``` python3 manage.py test ```
