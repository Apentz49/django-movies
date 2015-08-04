from django.contrib import admin

# Register your models here.
from .models import Rater, Movie, Ratings

class RaterAdmin(admin.ModelAdmin):
    list_display = ('gender', 'age', 'occupation', 'zipcode')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genres')

class RatingsAdmin(admin.ModelAdmin):
    list_display = ('movie', 'movie_rating', 'rater',)



admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Ratings, RatingsAdmin)