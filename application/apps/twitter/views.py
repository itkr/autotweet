# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from application.module.twitter_api import TwitterAPI
from .forms import TweetForm


class SimpleTweetView(TemplateView):

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = TweetForm(request.POST)
        if form.is_valid():
            twitter = TwitterAPI(request.user)
            twitter.PostUpdates(form.cleaned_data['message'])

        return HttpResponseRedirect(reverse('index'))
