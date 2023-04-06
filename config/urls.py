from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter, SimpleRouter
from authors.views import AuthorModelViewSet
from TODO import views as views_todo
from TODO.views import CustomUserModelViewSet, ProjectModelViewSet, ToDo_notesModelViewSet
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from rest_framework.authtoken import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView


schema_view = get_schema_view(
   openapi.Info(
      title="TODO API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact(email="logist26rus@gmail.com"),
      license=openapi.License('MIT'),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-auth', include('rest_framework.urls')),
   path('views/api-view', views_todo.ProjectModelViewSet.as_view({'get': 'list'})),
   path('api/', include('TODO.urls')),
   path('api-token-auth/', views.obtain_auth_token),
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('graphql/', GraphQLView.as_view(graphiql=True)),
   path('', TemplateView.as_view(template_name='index.html'))


]
