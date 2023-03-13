from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import generics, permissions
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ToDo_notes, Project, CustomUser
from .serializers import CustomUserSerializer, ProjectSerializer, ToDo_notesSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from django_filters import rest_framework as filters
from rest_framework import generics

class CustomUserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100

class CustomUserModelViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin,
                             mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    pagination_class = CustomUserLimitOffsetPagination
    
    

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    def get_queryset(self):
        return Project.objects.filter(name__contains='JS')


class ToDo_notesLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class ToDo_notesModelViewSet(ModelViewSet):
    queryset = ToDo_notes.objects.all()
    serializer_class = ToDo_notesSerializer
    pagination_class = ToDo_notesLimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('id', 'create',)

class ToDoFilters(filters.FilterSet):
    class Meta:
        model = ToDo_notes
        fields = ('id', 'create',)