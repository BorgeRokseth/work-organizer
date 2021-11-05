from django.db import models
from django.conf import settings
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class Context(models.Model):
    name = models.CharField(max_length=25)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="contexts")
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=70)
    goal = models.TextField()
    done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="project")

    def __str__(self) -> str:
        return self.name


class NextAction(models.Model):
    description = models.TextField()
    done = models.BooleanField(default=False)
    context = models.ForeignKey(to=Context, on_delete=models.CASCADE, related_name="next_action")
    project = models.ForeignKey(to=Project, on_delete=models.SET_NULL, null=True, related_name="actions")
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="next_action")

    def __str__(self) -> str:
        return self.description