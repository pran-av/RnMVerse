# django library imports
from django.urls import path
#from django.views.generic import TemplateView

# project based imports
from .views import ShowQuery

urlpatterns = [
    path('', ShowQuery.as_view(), name = 'home'),
]

# From ..urls
