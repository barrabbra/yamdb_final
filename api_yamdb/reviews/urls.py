from django.urls import include, path
from rest_framework.routers import DefaultRouter

from reviews import views

router = DefaultRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet,
    basename='reviews')

router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet,
    basename='comments'
)
urlpatterns = [
    path('', include(router.urls)),
]
