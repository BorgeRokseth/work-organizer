from django.db import models
from django.conf import settings


class InItem(models.Model):
    description = models.TextField()
    procesesed = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="in_item", default=1)
