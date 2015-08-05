from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
from movierater.models import Rater, Movie, Rating

# Create your views here.
def list_movie(request):
    # all_ratings_list = Movie.all_ratings(request)
    # avg_rating = Movie.avg_rating(request).order_by('-rating')[:20]
    movie_list = Movie.objects.all()

    # return render(request, "movierater/list_movie.html",
    #               {"all_ratings_list": all_ratings_list, "avg_rating": avg_rating})
    return render(request, 'movierater/list_movie.html',
                  {"movie_list": movie_list})


def detail_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    return render(request, "movierater/detail_movie.html", {'movie': movie})

def rater_detail(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)

    return render(request, 'movierater/rater_detail.html',
                  {'age': rater.age, 'gender': rater.gender,
                   'occupation': rater.occupation, 'zip_code': rater.zip_code})