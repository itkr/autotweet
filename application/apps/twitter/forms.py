# -*- coding: utf-8 -*-
from django import forms
from django.forms import Textarea


class TweetForm(forms.Form):
    message = forms.CharField(
        widget=Textarea(attrs={'cols': 47, 'rows': 3}),
        max_length=140)
