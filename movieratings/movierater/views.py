import datetime
from django.core.urlresolvers import reverse_lazy
from django.db.models import Avg
from django.views.generic import ListView, DetailView, CreateView
from movierater.models import Rater, Movie, Rating, Category


class Top20(ListView):
    model = Movie
    template_name = "movierater/top_20_movies.html"
    queryset = Movie.objects.all().exclude(rating=None).annotate(
        overall=Avg('rating__rating')).order_by('-overall')
    context_object_name = 'avg_rating'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(Top20, self).get_context_data(**kwargs)
        context['page_load'] = datetime.datetime.now()
        return context


class MovieGenres(ListView):
    model = Category
    context_object_name = 'category'
    template_name = 'movierater/movie_genres.html'
    paginate_by = 20


class MovieList(ListView):
    model = Movie
    template_name = "movierater/list_movie.html"
    queryset = Movie.objects.all().order_by('title')
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)
        context['page_load'] = datetime.datetime.now()
        return context


class MovieDetail(DetailView):
    model = Movie
    pk_url_kwarg = 'movie_id'
    template_name = 'movierater/detail_movie.html'


class RaterDetail(DetailView):
    model = Rater
    pk_url_kwarg = 'rater_id'
    template_name = 'movierater/rater_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RaterDetail, self).get_context_data(**kwargs)
        return context

class RaterList(ListView):
    model = Movie
    template_name = "movierater/list_rater.html"
    queryset = Rater.objects.all()
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(RaterList, self).get_context_data(**kwargs)
        context['page_load'] = datetime.datetime.now()
        return context


class NewRating(CreateView):
    model = Rating
    fields = ('rating', 'movie')
    success_url = reverse_lazy('top20')
    template_name = "movierater/user_rating.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.posted_at = datetime.datetime.now()
        return super(NewRating, self).form_valid(form)
