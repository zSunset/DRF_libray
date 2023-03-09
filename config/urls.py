from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authors.views import AuthorModelViewSet
from TODO.views import CustomUserModelViewSet, ProjectModelViewSet, ToDo_notesModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)

router_1 = DefaultRouter()
router_1.register('appuser', CustomUserModelViewSet)

router_2 = DefaultRouter()
router_2.register('project', ProjectModelViewSet)

router_3 = DefaultRouter()
router_3.register('todonotes', ToDo_notesModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/', include(router_1.urls)),
    path('api/', include(router_2.urls)),
    path('api/', include(router_3.urls)),
    
]
