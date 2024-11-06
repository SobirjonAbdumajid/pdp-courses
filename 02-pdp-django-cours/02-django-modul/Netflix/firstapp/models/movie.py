from django.db import models
from .actor import Actor


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    imdb = models.FloatField()
    genre = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor, related_name='actor')
    watched = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
