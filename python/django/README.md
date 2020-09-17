# Django
_A high-level Python Web framework that encourages rapid development_

## mysite/__init__.py
_An empty file that tells Python that this directory should be considered as a Python package_

## mysite/settings.py
- Settings/configuration for this Django project

## mysite/urls.py
_A “table of contents” of your Django-powered site_
- The URL declarations for this Django project

## Database
- [Link](https://realpython.com/django-migrations-a-primer/)
- Django is designed to work with a **relational database**, like PostgreSQL, MySQL, or SQLite
- Django comes with an object-relational mapper(ORM), which maps the relational database to the world of object oriented programming
- Instead of defining database tables in SQL, you write **Django models** in Python. Your models define database fields, which correspond to the columns in their database tables
  <img src="https://files.realpython.com/media/model_to_schema.4e4b8506dc26.png" height="300px">
- Creating the database tables to store your Django models is the job of a database migration

### `makemigrations`
_Create migrations for changes_

### Migration
- How Django stores changes to your models (and thus your database schema) - they’re files on disk

### `migrate`
_Apply changes to the database_
- Looks at the `INSTALLED_APPS` setting and creates any necessary database tables according to the database settings in the mysite/settings.py file

