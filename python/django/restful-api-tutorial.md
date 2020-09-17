# Test Driven Development of a Django RESTful API
1. Django Project Setup
2. Django App and REST Framework Setup
3. Database and Model Setup

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










