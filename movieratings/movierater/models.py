
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg


class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Rater(models.Model):

    user = models.OneToOneField(User, primary_key=True)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()
    occupation = models.CharField(max_length=3)
    zip_code = models.CharField(max_length=20)

    def all_ratings(self):
        return self.rating_set.all()

    def __str__(self):
        return "ID: {} Gender: {} Age: {} Occupation: {} Zipcode: {}"\
                .format(self.id, self.gender, self.age, self.occupation, self.zip_code)



class Movie(models.Model):

    genre = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    tag = models.ManyToManyField(Category)

    def all_rater_ratings(self):
        return self.rating_set.all()

    def avg_rating(self):
        avg_rating = self.rating_set.all().aggregate(Avg('rating'))['rating__avg']
        if avg_rating != None:
            return avg_rating

    def __str__(self):
        return "{} {} {}".format(self.id, self.title, self.genre)


class Rating(models.Model):

    rating = models.IntegerField()
    movie = models.ForeignKey(Movie)
    rater = models.ForeignKey(Rater)
    timestamp = models.IntegerField()

    def __str__(self):
        return "Rater:{} Movie:{} Rating:{} Timestamp:{}".format(self.rater.id,
                                                                 self.movie.title,
                                                                 self.rating,
                                                                 self.timestamp)





# for rater in Rater.objects.all():
#     rater.user = User.objects.create_user(username=rater.pk, email="yo@tiy.com", password="1")
#     rater.save()
#     print("User Created")

