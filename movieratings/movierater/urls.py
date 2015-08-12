from django.conf.urls import url
from movierater.views import MovieList, RaterList, MovieDetail, RaterDetail, \
    Top20, NewRating, MovieGenres

urlpatterns = [
    url(r'^$', MovieList.as_view(), name='list_movie'),
    url(r'^top20/$', Top20.as_view(), name='top20'),
    url(r'^user/$', RaterList.as_view(), name='list_rater'),
    url(r'^(?P<movie_id>[0-9]+)/', MovieDetail.as_view(), name="detail_movie"),
    url(r'^user/(?P<rater_id>[0-9]+)/', RaterDetail.as_view(),
        name="rater_detail"),
    url(r'^user_rating/$', NewRating.as_view(), name='new_rating'),
    url(r'^genre/$', MovieGenres.as_view(), name='movie_genres'),
]
