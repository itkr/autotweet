from django.conf.urls import patterns, include, url
from .views import SimpleTweetView

urlpatterns = patterns('',
    url(r'^/tweet$',  SimpleTweetView.as_view(), name='twitter-tweet'),
)
