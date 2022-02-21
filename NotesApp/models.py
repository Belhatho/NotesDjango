from django.db import models
from django.db.models.base import Model


# Create your models here.

class Notes(models.Model):
    name = models.CharField(max_length=50)
    createdAt = models.TimeField
    content = models.TextField

    def __str__(self):
        return str(self.name) + ' ' + str(self.createdAt) + ' ' + str(self.content)
