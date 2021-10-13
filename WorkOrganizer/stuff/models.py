from django.db import models


class InItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
