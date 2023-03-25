from django.contrib import admin
from .models import CustomUser
from rest_framework.authtoken.admin import TokenAdmin

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_active', 'date_joined']
    ordering = ['-date_joined']


TokenAdmin.raw_id_fields = ['user']