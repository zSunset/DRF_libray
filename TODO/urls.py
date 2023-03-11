from django.urls import path
from . import views
from .apps import TodoConfig
from rest_framework.routers import DefaultRouter

app_name = TodoConfig.name


urlpatterns = []
