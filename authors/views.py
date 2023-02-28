from rest_framework.viewsets import ModelViewSet
from .models import Author, CustomUser
from .serializers import AuthorModelSerializer

class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = AuthorModelSerializer