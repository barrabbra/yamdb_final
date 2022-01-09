from django.shortcuts import get_object_or_404
from rest_framework import serializers

from titles.models import Title

from .models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    title = serializers.SlugRelatedField(
        slug_field='id', read_only=True)

    def validate(self, data):
        if self.context['request'].method == 'PATCH':
            return data

        user = self.context['request'].user
        title = get_object_or_404(
            Title,
            pk=self.context['request'].parser_context['kwargs'].get('title_id')
        )
        if Review.objects.filter(author=user, title=title).exists():
            raise serializers.ValidationError(
                f'Вы уже написали отзыв к произведению {title.name}'
            )
        return data

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    review = serializers.SlugRelatedField(
        slug_field='id', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
