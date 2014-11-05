from django.conf.urls import patterns, include, url
from .views import IndexView, LogoutView

urlpatterns = patterns('',
    url(r'^$',  IndexView.as_view(), name='index'),
    url(r'^/logout$',  LogoutView.as_view(), name='logout'),
)
