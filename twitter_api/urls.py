from django.urls import include, path

from rest_framework import routers

from .views import  get_tweet_stats


urlpatterns = [
    path('twitter_stats/', get_tweet_stats, name='twitter-stats'),
]