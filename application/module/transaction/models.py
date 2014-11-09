# -*- coding: utf-8 -*-
from django.db import models
from application.submodules.tools.db import UserHasManyModelMixin


class Transaction(UserHasManyModelMixin):

    class Meta:
        app_label = "transaction"

    time_id = models.IntegerField(null=True, default=None)
    text = models.TextField(max_length=140, default='')
    enable = models.BooleanField(default=True)
    remaining_count = models.PositiveIntegerField(null=True, default=None)

    def update(self, **kwargs):

        """
        トランザクションに更新を書ける
        for_update()必要
        commit_on_success必要
        """

        self.objects.update(**kwargs)
        self.save()
        return self

    def decrement_remaining_count(self):

        """
        残り回数を減算
        Noneや0のときは減算しない
        for_update()必要
        commit_on_success必要
        """

        if self.remaining_count:
            self.remaining_count -= 1
            self.save()
        return self
