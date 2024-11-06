from django.test import TestCase
from firstapp.models import Movie, Comment, Actor
from django.urls import reverse
from rest_framework.test import APIClient
from firstapp.serializers import MovieSerializer, CommentSerializer, ActorSerializer


class TestMovieSerializer(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            name='Abu Ali Ibn Sino',
            year=1980,
            genre='Drama',
            imdb=7.5
        )

    def test_data(self):
        data = MovieSerializer(self.movie).data
        assert data['id'] is not None
        assert data['name'] == "Abu Ali Ibn Sino"
        assert data['year'] == 1980
        assert data['genre'] == "Drama"
        assert data['imdb'] == 7.5
        assert data['actors'] == []
        assert data['watched'] == 0




class MovieViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create sample movies
        Movie.objects.create(name="Movie 1", year=2000, genre="Action", imdb=6.5, watched=100)
        Movie.objects.create(name="Movie 2", year=2005, genre="Drama", imdb=7.5, watched=50)

    def test_movie_list(self):
        url = reverse('movie-list')  # Replace 'movie-list' with the actual name of the route for listing movies
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], "Movie 1")
        self.assertEqual(response.data[1]['name'], "Movie 2")



    # def test_movie_search(self):
    #     actor = Actor.objects.create(name="John Doe", birthdate="1980-01-01", gender="M")
    #     movie = Movie.objects.create(name="Movie with Actor", year=2010, genre="Comedy", imdb=8.0)
    #     movie.actors.add(actor)
    #
    #     # Search by movie name
    #     url = f"{reverse('movie-list')}?search=Movie with Actor"
    #     response = self.client.get(url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data[0]['name'], "Movie with Actor")
    #
    #     # Search by actor name
    #     url = f"{reverse('movie-list')}?search=John Doe"
    #     response = self.client.get(url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data[0]['name'], "Movie with Actor")

    # def test_movie_order_by_imdb(self):
    #     Movie.objects.create(name="High IMDb Movie", year=2000, genre="Sci-Fi", imdb=9.0)
    #     Movie.objects.create(name="Low IMDb Movie", year=2005, genre="Horror", imdb=5.0)
    #
    #     # Sort by IMDb in descending order
    #     url = f"{reverse('movie-list')}?ordering=-imdb"
    #     response = self.client.get(url)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response.data[0]['name'], "High IMDb Movie")
    #     self.assertEqual(response.data[1]['name'], "Low IMDb Movie")

class TextActorSerializer(TestCase):
    def setUp(self):
        pass

    def test_is_valid(self):
        data = {
            'name': 'Sobirjon',
            'birthdate': '2005-03-05',
            'gender': 'Male'
        }
        serializer = ActorSerializer(data=data)

        self.assertTrue(serializer.is_valid())

    def test_is_not_valid(self):
        data = {
            'name': 'Sobirjon',
            'birthdate': '1990-01-01',
            'gender': 'Male'
        }
        serializer = ActorSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        print(serializer.errors)

# name = models.CharField(max_length=255)
# birthdate = models.DateField()
# gender = models.CharField(max_length=100)
