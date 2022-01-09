from django.contrib.auth import get_user_model
from django.db.models import Avg
from rest_framework import filters, mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from titles import serializers
from users.permissions import IsAdminOrReadOnly
from .filters import TitleFilter
from .models import Category, Genre, Title

User = get_user_model()


class TitleViewSet(ModelViewSet):

    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')).order_by('id')
    filterset_class = TitleFilter
    filterset_fields = ['category', 'genre', 'year', 'name']
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action in ('create', 'partial_update'):
            return serializers.TitleSerializerCreate
        return serializers.TitleSerializerRead


class ApiViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.DestroyModelMixin):
    lookup_field = 'slug'
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]


class CategoryViewSet(ApiViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = serializers.CategorySerializer


class GenreViewSet(ApiViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer
