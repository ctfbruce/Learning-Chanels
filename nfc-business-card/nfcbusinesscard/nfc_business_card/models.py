from django.db import models

# Create your models here.

from django.db import models

class UserMessage(models.Model):
    custom_hash = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
