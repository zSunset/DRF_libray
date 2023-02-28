from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthotModelViewSet
from .apps import AuthorsConfig

app_name = AuthorsConfig.name


router = DefaultRouter()
router.register('authors', AuthotModelViewSet)

urlpatterns = [
    
]
