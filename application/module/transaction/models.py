# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from application.submodules.tools.db import UserHasManyModelMixin


class Transaction(UserHasManyModelMixin):

    class Meta:
        app_label = "transaction"

    time_id = models.IntegerField(null=True, default=None)
    text = models.TextField(max_length=140, default='')
    enable = models.BooleanField(default=True)
    remaining_count = models.PositiveIntegerField(null=True, default=None)

    start_at = models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)

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

    def is_in_term(self, target_datetime=None):

        """
        指定したdatetimeが期間内に含まれているか
        datetimeを指定しなかった場合は現在の日時を使用する
        """

        if target_datetime is None:
            target_datetime = datetime.now()
        # どちらも指定なし
        if not self.start_at and not self.end_at:
            return True
        # startのみ指定
        if self.start_at and not self.end_at:
            return self.start_at <= target_datetime
        # endのみ指定
        if not self.start_at and self.end_at:
            return target_datetime <= self.start_at
        # どちらも指定あり
        if self.start_at and self.end_at:
            return self.start_at <= target_datetime <= self.end_at

    @property
    def enable(self):
        return self.is_in_term(datetime.now())
