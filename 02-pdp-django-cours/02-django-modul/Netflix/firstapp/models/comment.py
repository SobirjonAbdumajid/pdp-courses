from django.db import models
from .movie import Movie
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.movie.name}"
