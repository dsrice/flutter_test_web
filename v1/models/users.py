from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from core.models import TimeStampedModel
from v1.manager import CustomUserManager


# ユーザ情報
class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    loginid = models.CharField(unique=True, max_length=50)

    objects = CustomUserManager()

    EMAIL_FILED = 'loginid'
    USERNAME_FIELD = 'loginid'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
