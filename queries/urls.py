# django library imports
from django.urls import path
#from django.views.generic import TemplateView

# project based imports
from .views import get_character

#print("Inside app URLconfig")
urlpatterns = [
    #path('', ShowQuery.as_view(template_name = 'home.html'), name = 'home'),
    path('queries/', get_character),
]
#print("Inside app end of URLconfig")

# From ..urls
