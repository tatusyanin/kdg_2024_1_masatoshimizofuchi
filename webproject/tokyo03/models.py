from django.db import models

# Create your models here.
from django.db import models

class Special(models.Model):
    title = models.CharField(max_length = 30)
    text = models.TextField()
    thumbnail = models.ImageField()
