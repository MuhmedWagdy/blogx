from django.db import models

from django.utils import timezone

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField(max_length=3000)
    created_date = models.DateTimeField(default=timezone.now)
    draft = models.BooleanField(default=True)