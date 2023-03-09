from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework import generics, permissions
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ToDo_notes, Project, CustomUser
from .serializers import CustomUserSerializer, ProjectSerializer, ToDo_notesSerializer
from rest_framework.viewsets import ModelViewSet

class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ToDo_notesModelViewSet(ModelViewSet):
    queryset = ToDo_notes.objects.all()
    serializer_class = ToDo_notesSerializer