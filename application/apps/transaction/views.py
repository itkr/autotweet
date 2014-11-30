# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from application.module.transaction import Transaction

TEMPLATE_DIRECTORY = 'transaction'


class ListView(TemplateView):

    template_name = '/'.join([TEMPLATE_DIRECTORY, 'list.html'])

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        return self.render_to_response(context)

    def get_context_data(self, request, **kwargs):
        if request.session.get('social_auth_last_login_backend') == 'twitter':
            user = request.user
            return {
                'user': user,
                'transactions': Transaction.get_by_user_id(user.id),
            }
        return {}


class DetailView(TemplateView):

    template_name = '/'.join([TEMPLATE_DIRECTORY, 'detail.html'])

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        return self.render_to_response(context)

    def get_context_data(self, request, **kwargs):
        if request.session.get('social_auth_last_login_backend') == 'twitter':
            user = request.user
            transaction_id = kwargs.get('transaction_id')
            try:
                transaction = Transaction.get_by_user_id(user.id, id=transaction_id)[0]
            except Transaction.DoesNotExist:
                # TODO: 処理
                raise
            return {
                'user': user,
                'transaction': transaction,
            }
        return {}


class UpdateView(TemplateView):

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('transaction-list'))
