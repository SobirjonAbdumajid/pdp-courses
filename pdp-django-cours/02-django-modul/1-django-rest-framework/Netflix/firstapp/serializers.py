from .models import Movie, Actor
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'birthdate', 'gender')

    def validate_birthdate(self, value):
        year = value.year
        month = value.month
        day = value.day
        print(year, type(month), type(day))
        if day != 5 or year != 2005 or month != 3:
            raise ValidationError('Your birthdate must be 2005-03-05')

        return value

class MovieSerializer(serializers.ModelSerializer):
    # actors = ActorSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'name', 'year', 'imdb', 'genre', 'actors', 'watched')

    def validate_imdb(self, value): # we usually use validate for
        if value < 5:
            raise ValidationError('The imdb should be more than 5 at lest')

        return value