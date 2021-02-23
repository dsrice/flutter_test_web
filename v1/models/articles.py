from django.db import models
from core.models import TimeStampedModel


class Article(TimeStampedModel):
    """
    記事情報
    """
    title = models.CharField(max_length=100, help_text="記事のタイトル")
    body = models.TextField()
    push_title = models.CharField(max_length=100, help_text="プッシュ通知のタイトル")
    push_body = models.CharField(max_length=300, help_text="プッシュ通知の本文")
