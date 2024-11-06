# from django.test import TestCase, Client
# from firstapp.models import Actor
#
#
# class TestActorViewSet(TestCase):
#     def setUp(self) -> None:
#         self.actor = Actor.objects.create(name='Test Actor')
#         self.client = Client()
#
#     def test_get_all_actors(self):
#         response = self.client.get('/actors/')
#         data = response.data
#         print(data)


from django.test import TestCase, Client
from firstapp.models import Actor, Comment


class TestActorViewSet(TestCase):
    def setUp(self) -> None:
        # Provide values for all required fields
        self.actor = Actor.objects.create(
            name='Test Actor',
            birthdate='1980-01-01',
            gender='M'
        )
        self.client = Client()

    def test_get_all_actors(self):
        response = self.client.get('/actors/')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertIsNotNone(data[0]["id"])
        self.assertEqual(data[0]["name"], "Test Actor")
        self.assertEqual(data[0]["birthdate"], "1980-01-01")
        self.assertEqual(data[0]["gender"], "M")




    # movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    # text = models.TextField()
    # created_date = models.DateTimeField()