from rest_framework import serializers
from .models import ToDo_notes, Project
from authors.models import CustomUser

class ToDo_notesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo_notes
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"