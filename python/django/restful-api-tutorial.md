# Test Driven Development of a Django RESTful API
1. [Django Project Setup](#django-project-setup)
2. [Django App and REST Framework Setup](#django-app-and-rest-framework-setup)
3. [Database and Model Setup](#database-and-model-setup)

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
