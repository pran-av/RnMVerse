# import library to process post requests
#import requests
#import json

# import django libraries
from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse

# Import project classes
from .services import YourCharacter
#print(YourCharacter)

# Class based views require project templates
#class GetCharacter(generic.TemplateView):
    #template_name = 'character.html'
def character_detail_view(request):
    #context = {}
    #context["character_info"] = YourCharacter.get_character_info()
    context = {
        #'characters' : YourCharacter.executeQuery(5),
        'character_info' : YourCharacter.get_character_info(),
        'character_episodes' : YourCharacter.get_character_episodes(),
    }
    print("\nContext:", context)
    return render(request, "queries/character.html", context)

#character_detail_view()
"""
# Definition based views require app templates
def character_detail_view(request):
    #print(YourCharacter.recipe)
    rcp = YourCharacter.recipe
    print("Recipe in Views:", rcp)
    context = {}
    context["data"] = YourCharacter.executeQuery(YourCharacter.recipe)
    print("Body:", context)
    #query["data"] = context
    return render(request, "queries/character.html", context)



query = {}
query["data"] = {}
query["data"]["data"] = {}
query["data"]["data"]["character"] = {}

def get_character(request):
    #create a dictionary
    recipe = YourCharacter.cookery()
    print("View: The random number is:", recipe)
    context = YourCharacter.executeQuery(recipe)


    #context = {
    #    'character' : YourCharacter.executeQuery(recipe)
    #}

    # assign an object data
    #context["data"] = YourCharacter.objects.get(id = id)
    #context["data"]  = YourCharacter.executeQuery(recipe)
    print("Context:", context)
    return context
    #return render(request, 'queries/character.html', context)

CREATION SCRIPT

class ShowQuery(generic.TemplateView):
    model = YourCharacter

    def request_data():
        recipe = YourCharacter.cookery()
        print("In request_data method", recipe)
        st, bd = YourCharacter.executeQuery(recipe)
        print("Status:", st)

        return st, bd

ShowQuery.request_data()

print(YourCharacter.status)


# Program flow passes to . urls
"""
