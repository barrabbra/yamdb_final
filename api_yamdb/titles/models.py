import datetime as dt

from django.core import exceptions
from django.db import models


def year_validator(value):
    curr_year = dt.date.today().year
    if value > curr_year:
        raise exceptions.ValidationError(
            f'Year value should be les or equal {curr_year}')


class Genre(models.Model):
    name = models.CharField('Genre', max_length=200)
    slug = models.SlugField('Slug', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Category(models.Model):
    name = models.CharField('Category', max_length=200)
    slug = models.SlugField('Slug', unique=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Title', max_length=200)
    year = models.PositiveSmallIntegerField('Year',
                                            validators=[year_validator],
                                            )

    genre = models.ManyToManyField(Genre, related_name="genres")
    description = models.TextField('Description')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='categories',
    )

    class Meta:
        ordering = ['id']
