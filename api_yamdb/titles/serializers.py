from rest_framework import serializers

from .models import Category
from .models import Genre
from .models import Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['id']
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['id']
        model = Genre


class BaseTitleSerializer(serializers.ModelSerializer):

    rating = serializers.FloatField(read_only=True)

    class Meta:
        fields = ['rating',
                  'name',
                  'year',
                  'genre',
                  'description',
                  'category',
                  'id']
        model = Title


class TitleSerializerCreate(BaseTitleSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True
    )


class TitleSerializerRead(BaseTitleSerializer):
    category = CategorySerializer()
    genre = GenreSerializer(many=True)
