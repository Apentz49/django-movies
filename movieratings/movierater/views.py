import datetime
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Avg
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, RequestContext
from django.views.generic import ListView, DetailView
from movierater.forms import RatingForm
from movierater.models import Rater, Movie, Rating

# Create your views here

def top_20_movies(request):
    movie_list = Movie.objects.all()
    avg_rating = movie_list.annotate(overall=Avg('rating__rating')).order_by('-overall')[:20]


    return render(request, 'movierater/top_20_movies.html',
                  {"movie_list": movie_list, "avg_rating": avg_rating})


# def list_movie(request):
#     movie_list = Movie.objects.all().order_by('title')
#
#     return render(request, 'movierater/list_movie.html',
#                   {"movie_list": movie_list})

class MovieList(ListView):
    model = Movie
    template_name = "movierater/list_movie.html"
    queryset = Movie.objects.all().order_by('title')
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)
        context['page_load'] = datetime.datetime.now()
        return context


# def detail_movie(request, movie_id):
#     movie = Movie.objects.get(pk=movie_id)
#     avg_ratings = movie.avg_rating()
#     all_ratings = movie.all_rater_ratings()
#
#
#     return render(request, "movierater/detail_movie.html",
#                   {'movie': movie, 'avg_ratings': avg_ratings, 'all_ratings': all_ratings})


class MovieDetail(DetailView):
    model = Movie
    pk_url_kwarg = 'movie_id'
    # Default chirp_detail.html
    template_name = 'movierater/detail_movie.html'


class RaterDetail(DetailView):
    model = Movie
    pk_url_kwarg = 'rater_id'
    template_name = 'movierater/rater_detail.html'

# def rater_detail(request, rater_id):
#     rater = Rater.objects.get(pk=rater_id)
#
#
#     return render(request, 'movierater/rater_detail.html',
#                   { 'rater': rater})
#
# def list_rater(request):
#     rater_list = Rater.objects.all()
#     return render(request, 'movierater/list_rater.html',
#                   {"rater_list": rater_list})


class RaterList(ListView):
    model = Movie
    template_name = "movierater/list_rater.html"
    queryset = Rater.objects.all()
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(RaterList, self).get_context_data(**kwargs)
        context['page_load'] = datetime.datetime.now()
        return context



@login_required(login_url='/login')
def new_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)

        if form.is_valid():
            rating = form.save(commit=False)
            rating.movie_id = Movie.pk
            rating.rater_id = request.user.rater.id
            rating.save()

            return HttpResponseRedirect(reverse('detail_movie', args=['movie_id']))

    else:
        form = RatingForm()
    return render(request, 'movierater/user_rating.html', {'form':form, 'movie': Movie})