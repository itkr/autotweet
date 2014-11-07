# -*- coding: utf-8 -*-
from django import forms


class TweetForm(forms.Form):
    message = forms.CharField(max_length=140)
