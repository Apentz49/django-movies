from django.contrib import admin

# Register your models here.
from .models import Rater, Movie, Rating

class RaterAdmin(admin.ModelAdmin):
    list_display = ('gender', 'age', 'occupation', 'zip_code')

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rating', 'rater', 'timestamp')



admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
