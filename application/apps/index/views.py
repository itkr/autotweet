# -*- coding: utf-8 -*-
from django.views.generic import TemplateView
from application.module.transaction import Transaction
# TODO: dir
from application.apps.twitter.forms import TweetForm


TEMPLATE_DIRECTORY = 'root'


class IndexView(TemplateView):
    template_name = '/'.join([TEMPLATE_DIRECTORY, 'index.html'])

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.get(request, args, kwargs)

    def get_context_data(self, request, **kwargs):
        if request.session.get('social_auth_last_login_backend') == 'twitter':
            user = request.user
            return {
                'user': user,
                'form': TweetForm,
                'transactions': Transaction.get_by_user_id(user.id),
            }
        return {}
