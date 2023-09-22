from django.db import models
from .base import BaseModel


class File(BaseModel):
    file = models.FileField(upload_to="uploads/")
    processed = models.BooleanField(default=False)