"""This module creates database models for the QR app."""
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class UploadFile(models.Model):
    """Model for uploaded files."""
    name = models.CharField(max_length=255)
    image = CloudinaryField(
        'image',
        folder="uploads/",
        allowed_formats=["jpg", "png", "jpeg"],
        transformation={"quality": "auto"},
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"
