# Test Driven Development of a Django RESTful API
_Creates a Django puppies app with a RESTful API_

1. [Django Project Setup](#django-project-setup)
2. [Django App and REST Framework Setup](#django-app-and-rest-framework-setup)
3. [Database and Model Setup](#database-and-model-setup)
4. [Serializers](#serializers)
5. [RESTful Structure](#restful-structure)
6. [Routes](#routes)
7. [Browsable API](#browsable-api)
8. [Testing](#testing)

## Django Project Setup
1. Create and activate a virtualenv
```shell
mkdir django-puppy-store
cd django-puppy-store
python3.7 -m venv env
source env/bin/activate
```

2. Install Django and set up a new project
```shell
pip3.7 install django
django-admin startproject puppy_store
```

The current project structure should look like this:

```shell
└── puppy_store
    ├── manage.py
    └── puppy_store
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## Django App and REST Framework Setup
1. Creating the puppies app and installing REST Framework inside the virtualenv
```shell
cd puppy_store
python3.7 manage.py startapp puppies
pip3.7 install djangorestframework
```

2. Configure the Django project to make use of REST Framework
- Add the puppies app and rest_framework to the INSTALLED_APPS section within `puppy_store/puppy_store/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    ...,
    'puppies',
    'rest_framework'
]
```

- Define global settings for REST Framework in a single dictionary in the `settings.py` file
```python
    'DEFAULT_PERMISSION_CLASSES': [],  # allows unrestricted access to the API
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'  # sets the default test format to JSON for all requests
}
```

> Unrestricted access is fine for local development, but in a production environment you may need to restrict access to certain endpoints

- The current project structure should now look like:
```shell
└── puppy_store
    ├── manage.py
    ├── puppies
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── puppy_store
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py
```

## Database and Model Setup
1. Use SQLite database, which is included in macOS and Mac OS X by default
2. Define a puppy model with some basic attributes in `django-puppy-store/puppy_store/puppies/models.py`:
```python
from django.db import models


class Puppy(models.Model):
    """
    Puppy Model
    Defines the attributes of a puppy
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_breed(self):
        return self.name + ' belongs to ' + self.breed + ' breed.'

    def __repr__(self):
        return self.name + ' is added.'
```

3. Apply the migration
```shell
python3.7 manage.py makemigrations
python3.7 manage.py migrate
```

## Sanity Check
- Verify that the puppies_puppy has been created
    - connect to the database
    ```shell
    sqlite3 db.sqlite3
    ```
    - check all existing tables
    ```sqlite
    .tables
    ```
    -  `CONTROL + D` to exit sqlite

- Write a quick unit test for the Puppy model
    - Create new file called `test_models.py` in a new folder called `tests` within `django-puppy-store/puppy_store/puppies`
        ```python
        from django.test import TestCase
        from ..models import Puppy


        class PuppyTest(TestCase):
            """ Test module for Puppy model """

            def setUp(self):
                Puppy.objects.create(
                    name='Casper', age=3, breed='Bull Dog', color='Black')
                Puppy.objects.create(
                    name='Muffin', age=1, breed='Gradane', color='Brown')

            def test_puppy_breed(self):
                puppy_casper = Puppy.objects.get(name='Casper')
                puppy_muffin = Puppy.objects.get(name='Muffin')
                self.assertEqual(
                    puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
                self.assertEqual(
                    puppy_muffin.get_breed(), "Muffin belongs to Gradane breed.")
        ```
    - Remove the tests.py file from `django-puppy-store/puppy_store/puppies`
    - Add an `__init__.py` file to `tests`
    - Run the test
        ```shell
        python3.7 manage.py test
        ```

## Serializers
_Validates the model querysets and produces Pythonic data types to work with_

- Create a file `django-puppy-store/puppy_store/puppies/serializers.py`
```python
from .models import Puppy

class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = ('name', 'age', 'breed', 'color', 'created_at', 'updated_at')
```

## RESTful Structure
- In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. 

|Endpoint|HTTP Method|CRUD Method|Result|
|---|---|---|---|
|puppies|GET|READ|Get all puppies|
|puppies/:id|GET|READ|Get a single puppy|
|puppies|POST|CREATE|Add a single puppy|
|puppies/:id|PUT|UPDATE|Update a single puppy|
|puppies/:id|DELETE|DELETE|Delete a single puppy|

## Routes
### Create Views
- Create a skeleton of all view functions that return empty responses and map them with their appropriate URLs in `django-puppy-store/puppy_store/puppies/views.py`
```python
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Puppy
from .serializers import PuppySerializer

# @api_view: taks a list of HTTP methods the view should respond to, allows to c
onfigure how the request is processed
@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_puppy(request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single puppy
    if request.method == 'GET':
        serializer = PuppySerializer(puppy)
        return Response(serializer.data)

    # update details of a single puppy
    if request.method == 'PUT':
        serializer = PuppySerializer(puppy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single puppy
    elif request.method == 'DELETE':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_puppies(request):
    # get all puppies
    if request.method == 'GET':
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        return Response(serializer.data)
    # insert a new record for a puppy
    if request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'age': int(request.data.get('age')),
            'breed': request.data.get('breed'),
            'color': request.data.get('color')
        }
        serializer = PuppySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### Create URLs
- Create the respective URLs to match the views in `django-puppy-store/puppy_store/puppies/urls.py`:
    ```python
    from django.contrib import admin
    from django.urls import path
    from django.conf.urls import include, re_path

    urlpatterns = [
        path('admin/', admin.site.urls),
        re_path(r'^', include('puppies.urls')),
        re_path(r'^api-auth/',
                include('rest_framework.urls', namespace='rest_framework'))
    ]
    ```
- Update `django-puppy-store/puppy_store/puppy_store/urls.py`
    ```python
    # Create the respective URLs to match the views
    from django.urls import re_path
    from . import views

    # re_path(route, view, name)
    urlpatterns = [
        re_path(
            r'^api/v1/puppies/(?P<pk>[0-9]+)$',
            views.get_delete_update_puppy,
            name='get_delete_update_puppy'),
        re_path(
            r'^api/v1/puppies/$', views.get_post_puppies, name='get_post_puppies')
    ]
    ```

## Browsable API
_Generate human-friendly HTML output for each resource_
- Allows for easy browsing of resources, as well as forms for submitting data to the resources using POST, PUT, and DELETE 

## Testing
- Creating a new file, `django-puppy-store/puppy_store/puppies/tests/test_views.py` to hold all the tests for the views
    ```python
    import json
    from rest_framework import status
    from django.test import TestCase, Client
    from django.urls import reverse
    from ..models import Puppy
    from ..serializers import PuppySerializer
    ```
- Create a new test client
    ```python
    # Initialize the APIClient app
    client = Client()
    ```
- Test to verify the fetched records
    ```python
    class GetAllPuppiesTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')
        Puppy.objects.create(
            name='Rambo', age=2, breed='Labrador', color='Black')
        Puppy.objects.create(
            name='Ricky', age=6, breed='Labrador', color='Brown')

    def test_get_all_puppies(self):
        # get API response
        response = client.get(reverse('get_post_puppies'))
        # get data from db
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    ```
- Test inserting a new record
    ```python
    class CreateNewPuppyTest(TestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_payload = {
            'name': 'Muffin',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_create_valid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_puppy(self):
        response = client.post(
            reverse('get_post_puppies'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    ```
- Can also test out with the Browsable API
    - Navigate to http://localhost:8000/api/v1/puppies/
    - Within the POST form, submit the following
        ```python
        {
            "name": "Muffin",
            "age": 4,
            "breed": "Pamerion",
            "color": "White"
        }
        ```
    - <img src="browsable.png" height="300px">
- Test to update a record
    ```python
    class UpdateSinglePuppyTest(TestCase):
    """ Test module for updating an existing puppy record """

    def setUp(self):
        self.casper = Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        self.muffin = Puppy.objects.create(
            name='Muffy', age=1, breed='Gradane', color='Brown')
        self.valid_payload = {
            'name': 'Muffy',
            'age': 2,
            'breed': 'Labrador',
            'color': 'Black'
        }
        self.invalid_payload = {
            'name': '',
            'age': 4,
            'breed': 'Pamerion',
            'color': 'White'
        }

    def test_valid_update_puppy(self):
        response = client.put(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_puppy(self):
        response = client.put(
            reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    ```
    
