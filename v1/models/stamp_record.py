from django.db import models
from core.models import TimeStampedModel
from v1.models import User


class StampRecord(TimeStampedModel):
    """
    スタンプ履歴情報
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stamp = models.IntegerField()

    class Meta:
        db_table = "stamp_records"
