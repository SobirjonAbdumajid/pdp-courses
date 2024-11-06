from django.contrib import admin
from .models import Actor, Movie, Comment

# Register your models here.

admin.site.register([Actor, Movie, Comment])
