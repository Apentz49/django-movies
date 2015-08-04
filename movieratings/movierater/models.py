from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Rater(models.Model):

    gender = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    occupation = models.CharField(max_length=100)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.id

class Movie(models.Model):

    genres = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return "{} {}".format(self.id, self.title)

class Ratings(models.Model):

    movie_rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)

    def __str__(self):
        return "{}: {}".format(self.id, self.movie)
