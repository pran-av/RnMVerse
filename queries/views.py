# import library to process post requests
#import requests
#import json

# import django libraries
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse

# Import project classes
from .models import YourCharacter

def get_character(request):
    #create a dictionary
    recipe = YourCharacter.cookery()
    print("View: The random number is:",recipe)
    #context = YourCharacter.executeQuery(recipe)
    context = {}
    # assign an object data
    #context["data"] = YourCharacter.objects.get(id = id)
    context["data"]  = YourCharacter.executeQuery(recipe)
    print("Views: Context:", context)
    return JsonResponse(context, safe = False)
    #return render(request, 'queries/character.html', context)

#print("Views: Inside Views")
"""
CREATION SCRIPT

class ShowQuery(generic.TemplateView):
    model = YourCharacter
    #template_name = 'home.html'
    #st: int
    #bd: str
    #get_slug_field()
    def request_data():
        # Below statement prints body location
        #print(YourCharacter.body)
        recipe = YourCharacter.cookery()
        print("In request_data method", recipe)
        st, bd = YourCharacter.executeQuery(recipe)
        print("Status:", st)
        #YourCharacter.status = st
        #YourCharacter.body = bd

        return st, bd

    #print("Data:", bd)

# Printing before function call shows me the address
#print("Outside the class ShowQuery", YourCharacter.status)
ShowQuery.request_data()

print(YourCharacter.status)
#object.status
    #constructor
    #def __init__(self):
    #    print("Constructed!")
    #    self.st = st
    #    self.bd = bd


# Program flow passes to . urls
"""
