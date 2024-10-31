from django.contrib import admin
from .models import Actor, Movie

# Register your models here.

admin.site.register([Actor, Movie])