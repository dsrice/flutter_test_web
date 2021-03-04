from django.db import models
from core.models import TimeStampedModel
from v1.models import User


class StampTotal(models.Model):
    """
    スタンプ履歴情報
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = "stamp_total"
