from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Avg


class Rater(models.Model):

    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    occupation = models.CharField(max_length=3)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return "ID: {} Gender: {} Age: {} Occupation: {} Zipcode: {}"\
                .format(self.id, self.gender, self.age, self.occupation, self.zip_code)

class Movie(models.Model):

    genre = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def all_ratings(self):
        the_ratings = self.rating_set.all()
        return the_ratings

    def avg_rating(self):
        the_avg_rating = self.rating_set.all().aggregate(Avg('rating'))
        return the_avg_rating

    def __str__(self):
        return "{} {}".format(self.id, self.title)

class Rating(models.Model):

    rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)
    timestamp = models.IntegerField()

    def __str__(self):
        return "ID:{} MOVIE ID:{} MOVIE:{} TIMESTAMP:{}".format(self.id,self.movie.id,self.movie,self.timestamp)
