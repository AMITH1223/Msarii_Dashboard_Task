from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    created_at = models.DateField(default=timezone.now)
    progress = models.CharField(max_length=100)
    team_metrics = models.CharField(max_length=100)

class Task(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    end_date = models.DateField(default=timezone.now)

class Notification(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
