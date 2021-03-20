from django.urls import path

from .views import ShowQuery

urlpatterns = [
    path('<int:id>/', ShowQuery.as_view(), name = 'home'),
]
