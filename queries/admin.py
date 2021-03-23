from django.contrib import admin

# Register your models here.
from .models import YourCharacter

print("Registering class YC")
admin.site.register(YourCharacter)
