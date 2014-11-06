# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from application.module.twitter_api import TwitterAPI


class SimpleTweetView(TemplateView):

    def get(self, request, *args, **kwargs):
        if request.session.get('social_auth_last_login_backend') == 'twitter':
            twitter = TwitterAPI(request.user)
            twitter.send("test")
        return HttpResponseRedirect(reverse('index'))

    def post(self, request, *args, **kwargs):
        return self.get(request, args, kwargs)
