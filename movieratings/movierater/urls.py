from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'movierater.views.list_movie', name='listmovie'),
    url(r'(?P<movie_id>[0-9]+)/', 'movierater.views.detail_movie', name="detail_movie"),
    url(r'(?P<rater_id>[0-9]+)/', 'movierater.views.rater_detail', name="rater_detail"),
]