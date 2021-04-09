import json

# django library imports
from django.urls import path
from django.views.generic import TemplateView

# project based imports
from .services import YourCharacter
#from .views import GetCharacter
from .views import character_detail_view

#print("Inside app URLconfig")
urlpatterns = [
    #path('', ShowQuery.as_view(template_name = 'home.html'), name = 'home'),
    #path('queries/', get_character),
    #path('queries/character',
    #YourCharacter.as_view(template_name = 'queries/character.html'),
    #name = 'character'),
    path('', character_detail_view),
    #path('queries/character',
    #    GetCharacter.as_view(template_name = 'character_info.html'),
    #    name = 'character_info'),
]
#print("Inside app end of URLconfig")

# From ..urls
