from django.db import transaction
from rest_framework import status, viewsets, filters, generics
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Actor, Comment
from .serializers import MovieSerializer, ActorSerializer, CommentSerializer, CommentListSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from django.contrib.postgres.search import TrigramSimilarity
# from django_filters.rest_framework import DjangoFilterBackend


class MovieViewSet(ReadOnlyModelViewSet): # ModelViewSet
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter]
    # filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre']  # Enable filtering by genre
    ordering_fields = ['watched', '-watched']
    search_fields = ['name', 'actors__name'] # if: ['=name', 'actors__name'] = exact matches. ^ starts-with search
    # search_fields = ['^name', 'actors__name'] # if: ['=name', 'actors__name'] = exact matches. ^ starts-with search

    def get_queryset(self):
        queryset = Movie.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = Movie.objects.annotate(
                similarity=TrigramSimilarity('name', query),
            ).filter(similarity__gt=0.1).order_by('-similarity')
        return queryset

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


class ActorViewSet(ReadOnlyModelViewSet):
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


class AddCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentListSerializer

    def get_queryset(self):
        movie_id = self.request.query_params.get('movie_id')
        if movie_id:
            return Comment.objects.filter(movie_id=movie_id)
        return Comment.objects.none()


class DeleteCommentView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        # Ensure only the owner can delete their comment
        if comment.user != request.user:
            return Response(
                {"detail": "You do not have permission to delete this comment."},
                status=status.HTTP_403_FORBIDDEN
            )
        return super().delete(request, *args, **kwargs)


class CommentViewSet(ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()
