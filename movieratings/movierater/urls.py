from django.conf.urls import url
from movierater.views import MovieList, RaterList, MovieDetail, RaterDetail

urlpatterns = [
    url(r'^$', MovieList.as_view(), name='list_movie'),
    url(r'^top20/$', 'movierater.views.top_20_movies', name='top20'),
    url(r'^user/$', RaterList.as_view(), name='list_rater'),
    url(r'^(?P<movie_id>[0-9]+)/', MovieDetail.as_view(), name="detail_movie"),
    url(r'^user/(?P<rater_id>[0-9]+)/', RaterDetail.as_view(), name="rater_detail"),
    url(r'^user_rating/$', 'movierater.views.new_rating', name='new_rating'),
]