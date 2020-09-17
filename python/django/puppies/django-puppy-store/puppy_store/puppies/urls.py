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
