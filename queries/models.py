import requests
import json
import random

# django libraries
from django.db import models
from django.urls import reverse

# YourCharacter class stores/defines the query data output
class YourCharacter(models.Model):
    body = models.TextField()
    status = models.CharField(max_length = 100)
    #print("Models: Inside App models")

    def executeQuery(recipe):
        query = """
            query ($recipe:ID!) {
                character(id:$recipe){
                    name
                    image
                    type
                    status
                    species
                    episode{
                        episode
                        name
                    }
                }
            }
        """
        url = 'https://rickandmortyapi.com/graphql'
        variables = {'recipe': recipe}

        r = requests.post(url, json = {'query': query, 'variables': variables})

        body = r.json()
        #status = r.status_code
        return body

    def cookery():
        recipe = random.randrange(1, 150)
        return recipe

    # Return a string
    def __str__(self):
        return self.body

    # Declare a canonical url that points towards the object
    def get_absolute_url(self):
        return reverse('home', args = [str(self.id)])

# Program Flow passes to .views
