from django.db import models
from authors.models import CustomUser
from safedelete.models import SafeDeleteModel
from safedelete import SOFT_DELETE_CASCADE

class Project(models.Model):
    name = models.CharField(max_length=64, blank=False)
    link_to_repository = models.URLField(max_length=64, blank=True)
    user_set = models.ManyToManyField(CustomUser)
    
    def __str__(self) -> str:
        return self.name

class ToDo_notes(SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    header = models.CharField(max_length=64, blank=False)
    body = models.TextField(blank=False)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    user_set = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.header