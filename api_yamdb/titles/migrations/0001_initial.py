# Generated by Django 3.0.5 on 2021-05-01 09:21

from django.db import migrations, models
import django.db.models.deletion
import titles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Category')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Genre')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Title')),
                ('year', models.PositiveSmallIntegerField(validators=[titles.models.year_validator], verbose_name='Year')),
                ('description', models.TextField(verbose_name='Description')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='titles.Category')),
                ('genre', models.ManyToManyField(related_name='genres', to='titles.Genre')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
