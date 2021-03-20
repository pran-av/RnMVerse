import requests
import json

from django.db import models
from django.urls import reverse

# Create your models here.
class YourCharacter(models.Model):
    body = models.TextField
    status = models.CharField(max_length = 100)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('home', args = [str(self.id)])
