from django.db import models


# Create your models here.

class Notes(models.Model):
    name = models.CharField(max_length=50)
    createdAt = models.TimeField
    content = models.TextField

