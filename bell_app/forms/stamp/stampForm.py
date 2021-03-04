from bell_app.forms.commonForm import CommonForm
from django import forms

from v1.models import Article
from django_summernote.widgets import SummernoteWidget


class StampShowForm(CommonForm):
    """
    スタンプ管理画面用Form
    """
    userlist = None


