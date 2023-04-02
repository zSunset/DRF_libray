from rest_framework import  permissions, generics
from .models import ToDo_notes, Project, CustomUser
from .serializers import CustomUserSerializer, ProjectSerializer, ToDo_notesSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as filters
from django.db import IntegrityError
from django.contrib.auth.models import User
from authors.models import CustomUser
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

# class CustomUserLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 100

class CustomUserModelViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin,
                             mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # pagination_class = CustomUserLimitOffsetPagination
    
    

# class ProjectLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 10

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = ProjectSerializer
    # pagination_class = ProjectLimitOffsetPagination
    def get_queryset(self):
        return Project.objects.filter(name__contains='')


# class ToDo_notesLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 20

class ToDo_notesModelViewSet(ModelViewSet):
    queryset = ToDo_notes.objects.all()
    serializer_class = ToDo_notesSerializer
    # pagination_class = ToDo_notesLimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'create',)

class ToDoFilters(filters.FilterSet):
    class Meta:
        model = ToDo_notes
        fields = ('id', 'create',)
