# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from social_auth.models import UserSocialAuth


TEMPLATE_DIRECTORY = 'root'


class IndexView(TemplateView):
    template_name = '/'.join([TEMPLATE_DIRECTORY, 'index.html'])

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, args, kwargs)

    def get_context_data(self, request, **kwargs):
        print request.user.username
        if request.session.get('social_auth_last_login_backend') == 'twitter':
            auth = UserSocialAuth.objects.filter(user=request.user).get()
#            token = auth.tokens['access_token']
            return {
                'auth': auth,
                'user': request.user,
            }
        return {}


class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        logout(request)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, args, kwargs)
