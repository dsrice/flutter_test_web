from django.db import models
from core.models import TimeStampedModel
from v1.models import User


class Token(TimeStampedModel):
    """
    トークン情報
    """
    token = models.CharField(max_length=300, help_text="Firebaseのトークン情報")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "tokens"
