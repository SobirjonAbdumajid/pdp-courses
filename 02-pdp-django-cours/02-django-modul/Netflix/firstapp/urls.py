from django.urls import path, include
from .views import MovieViewSet, ActorViewSet, AddCommentView, CommentListView, DeleteCommentView, MovieActorAPIView, CommentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Movie application app",
        default_version='v1',
        description="This is the app description",
        contact=openapi.Contact(email='<sobirjon0305@gmail.com>'),
    ),
    public=True,
    permission_classes=(AllowAny,)
)


# Initialize the router
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'actors', ActorViewSet, basename='actor')
router.register(r'comment', CommentViewSet, basename='comment')

urlpatterns = [
    # Comment-related endpoints
    path('comments/add/', AddCommentView.as_view(), name='add-comment'),
    path('comments/list/', CommentListView.as_view(), name='list-comments'),
    path('comments/delete/<int:id>/', DeleteCommentView.as_view(), name='delete-comment'),

    # swagger and redoc
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),

    # Include the router URLs
    path('', include(router.urls)),

    # Movie-actor relationship endpoint
    path('movies/<int:id>/actors/', MovieActorAPIView.as_view(), name='movie-actors'),

    # Authentication endpoint
    path('auth/', obtain_auth_token),
]
