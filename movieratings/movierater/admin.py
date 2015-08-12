from django.contrib import admin
from .models import Rater, Movie, Rating, Category


class RaterAdmin(admin.ModelAdmin):
    list_display = ('gender', 'age', 'occupation', 'zip_code', 'user',)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rating', 'rater', 'timestamp',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)



admin.site.register(Rater, RaterAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Category, CategoryAdmin)
