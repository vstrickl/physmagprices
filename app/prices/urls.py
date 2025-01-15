"""This Module Creates URL Paths for the Landing Page."""
from django.urls import path

from . import views

# Create Your URL Patterns Here.
urlpatterns = [ path('', views.prices, name='prices') ]
