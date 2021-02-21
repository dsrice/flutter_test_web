from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
    モデルの基底クラス
    各テーブルにcreated_atなどを足すためのクラス
    """

    created_at = models.DateTimeField(default=timezone.now(), help_text="作成日")
    created_user_id = models.IntegerField(null=True, blank=True, help_text="作成ユーザID")
    updated_at = models.DateTimeField(auto_now=True, help_text="更新日")
    updated_user_id = models.IntegerField(null=True, blank=True, help_text="更新ユーザID")
    is_deleted = models.BooleanField(default=False, help_text="削除フラグ　０：未削除　１：削除済み")
    deleted_at = models.DateTimeField(null=True, blank=True, help_text="削除日")
    deleted_user_id = models.IntegerField(null=True, blank=True, help_text="削除ユーザID")

    class Meta:
        abstract = True

    def save(self, request=None, **kwargs):
        if request and request.user:
            user_id = request.user.id
            self.updated_user_id = user_id
            if not self.id:
                self.created_user_id = user_id

        super(TimeStampedModel, self).save(**kwargs)

    def logic_deleted(self, request=None, **kwargs):
        if request and request.user:
            user_id = request.user.id
            self.deleted_user_id = user_id

        self.deleted_at = timezone.now()
        self.is_deleted = True
        super(TimeStampedModel, self).save(**kwargs)
