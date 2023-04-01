from django.urls import path, include
from .views import ProjectModelViewSet, ToDo_notesModelViewSet, CustomUserModelViewSet
from .apps import TodoConfig
from rest_framework.routers import DefaultRouter

app_name = TodoConfig.name

router = DefaultRouter()
router.register('project', ProjectModelViewSet)
router.register('todonotes', ToDo_notesModelViewSet)
router.register('authors', CustomUserModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
