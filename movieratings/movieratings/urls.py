"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^movierater/', include('movierater.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'movierater.views.list_movie', name='listmovie'),
    url(r'(?P<movie_id>[0-9]+)/', 'movierater.views.detail_movie', name="detailmovie"),
    url(r'(?P<rater_id>[0-9]+)/', 'movierater.views.rater_detail', name="raterdetail"),
]
