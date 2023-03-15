from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from authors.views import AuthorModelViewSet
from TODO import views
from TODO.views import CustomUserModelViewSet, ProjectModelViewSet, ToDo_notesModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('appuser', CustomUserModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('todonotes', ToDo_notesModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('views/api-view', views.ProjectModelViewSet.as_view({'get': 'list'})),
    path('', include(router.urls)),
    
]
