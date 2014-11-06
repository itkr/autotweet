from django.conf.urls import patterns, include, url
from .apps.auth.views import LogoutView

urlpatterns = patterns('',
    # Login
    url(r'^logout$',  LogoutView.as_view(), name='logout'),

    # Application
    url(r'^$', include('application.apps.index.urls')),
    url(r'^twitter', include('application.apps.twitter.urls')),

    # Social
    url(r'', include('social_auth.urls')),
)
