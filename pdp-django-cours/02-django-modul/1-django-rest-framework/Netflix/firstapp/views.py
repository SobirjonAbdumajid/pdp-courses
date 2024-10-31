from django.db import transaction
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404

# Create your views here.

# class HelloWorldAPIView(APIView):
#     def get(self, request):
#         return Response(data={'message': 'Hello World!'})
#
#     def post(self, request):
#         # Use single quotes inside the f-string to avoid conflict with outer double quotes
#         message = f"Hello {request.data['name']}"
#         return Response(data={'greeting': message})

# class MovieAPIView(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#
#         return Response(data={'movies': serializer.data})
#
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response(data=serializer.data)
#
# class ActorAPIView(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#
#         return Response(data={'actors': serializer.data})
#
#     def post(self, request):
#         serializer = ActorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#         return Response(data=serializer.data)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=['GET'])
    def actors(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = ActorSerializer(movie.actors.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def watch(self, request, *args, **kwargs):
        movie = self.get_object()
        print(request, kwargs, args)
        with transaction.atomic():
            movie.watched += 1
            movie.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        movie = self.get_queryset()
        movies = movie.order_by('-watched')[:10]
        serializer = MovieSerializer(movies, many=True)

        return Response(data=serializer.data)


    @action(detail=True, methods=['POST'])
    def add_actor(self, request, pk=None):
        movie = self.get_object()
        actor_id = request.data.get('actor_id')
        actor = get_object_or_404(Actor, pk=actor_id)
        movie.actors.add(actor)
        return Response({'status': 'actor added'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def remove_actor(self, request, pk=None):
        movie = self.get_object()
        actor_id = request.data.get('actor_id')
        actor = get_object_or_404(Actor, pk=actor_id)
        movie.actors.remove(actor)
        return Response({'status': 'actor removed'}, status=status.HTTP_200_OK)

class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['GET'])
    def movies(self, request, *args, **kwargs):
        pass


class MovieActorAPIView(APIView):
    def get(self, request, id):
        movie = get_object_or_404(Movie, pk=id)
        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)