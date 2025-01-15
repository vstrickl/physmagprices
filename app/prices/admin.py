"""This Module Creates an Admin UI of the QR models."""
from django.contrib import admin

from .models import UploadFile

# Register your models here.
class UploadFileAdmin(admin.ModelAdmin):
    """Custom View for the Social Media Admin Panel."""
    search_fields = ('name',)
    list_display = ('name',)
admin.site.register(UploadFile, UploadFileAdmin)
