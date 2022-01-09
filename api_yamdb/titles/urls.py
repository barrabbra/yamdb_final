from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet
from .views import GenreViewSet
from .views import TitleViewSet

router = DefaultRouter()
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')

urlpatterns = [
    path('', include(router.urls))
]
