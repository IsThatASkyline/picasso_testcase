from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    uploaded_at = models.DateTimeField(db_index=True, default=timezone.now)

    class Meta:
        abstract = True
