# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('genre', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('occupation', models.CharField(max_length=3)),
                ('zip_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('timestamp', models.IntegerField()),
                ('movie', models.ForeignKey(to='movierater.Movie')),
                ('rater', models.ForeignKey(to='movierater.Rater')),
            ],
        ),
    ]
