from django.conf.urls import patterns, url
from .views import (
    ListView,
    DetailView,
    UpdateView,
)

urlpatterns = patterns('',
    url(r'^/list$',
        ListView.as_view(),
        name='transaction-list'),

    url(r'^/detail/(?P<transaction_id>\d+)$',
        DetailView.as_view(),
        name='transaction-detail'),

    url(r'^/update$',
        UpdateView.as_view(),
        name='transaction-update'),
)
