from django.urls import path, include
from .views import MovieViewSet
# from .views import MovieAPIView, ActorAPIView
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, ActorViewSet, MovieActorAPIView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'actors', ActorViewSet)

urlpatterns = [
    # path('movies/', MovieAPIView.as_view(), name='movie'),
    # path('actor/', ActorAPIView.as_view(), name='actor'),
    path('', include(router.urls)),
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name='movie-actors')
]
