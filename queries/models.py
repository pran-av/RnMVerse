#import requests
#import json
#import random

# django libraries
from django.db import models
from django.urls import reverse

# YourCharacter class stores/defines the query data output
class YC(models.Model):
    body = models.TextField()
    status = models.CharField(max_length = 100)
    print("Models: Inside App models")

    # Return a string
    def __str__(self):
        return self.body

    # Declare a canonical url that points towards the object
    def get_absolute_url(self):
        return reverse('home', args = [str(self.id)])

# Program Flow passes to .views
