# Django
_A high-level Python Web framework that encourages rapid development_

## mysite/__init__.py
_An empty file that tells Python that this directory should be considered as a Python package_

## mysite/settings.py
- Settings/configuration for this Django project

## mysite/urls.py
_A “table of contents” of your Django-powered site_
- The URL declarations for this Django project

## `makemigrations`
_Create migrations for changes_

### Migration
- How Django stores changes to your models (and thus your database schema) - they’re files on disk

## `migrate`
_Apply changes to the database_
- Looks at the `INSTALLED_APPS` setting and creates any necessary database tables according to the database settings in the mysite/settings.py file

