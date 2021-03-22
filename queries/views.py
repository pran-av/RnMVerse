# import library to process post requests
#import requests
#import json

# import django libraries
from django.shortcuts import render
from django.views import generic

# Import project classes
from .models import YourCharacter

class ShowQuery(generic.TemplateView):
    model = YourCharacter
    template_name = 'home.html'
    #st: int
    #bd: str

    recipe = YourCharacter.cookery()
    print("Outside of class", recipe)
    st, bd = YourCharacter.executeQuery(recipe)
    print("Status:", st)
    #print("Data:", bd)

    #constructor
    #def __init__(self):
    #    print("Constructed!")
    #    self.st = st
    #    self.bd = bd


# Program flow passes to . urls
