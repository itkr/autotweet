# -*- coding: utf-8 -*-
from django.conf import settings
import twitter
from social_auth.models import UserSocialAuth


class TwitterAPI(twitter.Api):

    def __init__(self, user):
        auth = UserSocialAuth.objects.filter(user=user).get()
        super(TwitterAPI, self).__init__(
            consumer_key=settings.TWITTER_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_CONSUMER_SECRET,
            access_token_key=auth.tokens["oauth_token"],
            access_token_secret=auth.tokens["oauth_token_secret"])
