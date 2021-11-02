# Import some packages needed
from django.contrib import admin
from django.urls import path, include
from . import views

# Define app name and url patterns
app_name = 'apps'
urlpatterns = [
  path('', views.index, name = 'index'),
]
