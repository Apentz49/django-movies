# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('genres', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('gender', models.CharField(max_length=200)),
                ('age', models.IntegerField(null=True)),
                ('occupation', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('movie_rating', models.IntegerField()),
                ('movie', models.ForeignKey(to='movierater.Movie')),
                ('rater', models.ForeignKey(to='movierater.Rater')),
            ],
        ),
    ]
