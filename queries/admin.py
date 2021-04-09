from django.contrib import admin

# Register your models here.
from .models import YC

#print("Registering class YC")
admin.site.register(YC)
