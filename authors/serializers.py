from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, CustomUser

class AuthorModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class CustomUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'