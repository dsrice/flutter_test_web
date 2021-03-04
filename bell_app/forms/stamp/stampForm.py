from bell_app.forms.commonForm import CommonForm
from django import forms

from v1.models import Article
from django_summernote.widgets import SummernoteWidget


class StampShowForm(CommonForm):
    """
    スタンプ管理画面用Form
    """
    userlist = None


class StampDetailForm(CommonForm):
    """
    スタンプ管理画面用Form
    """
    stamp_total = None
    user = None
    records = None
    page_obj =None

    stamp_count = forms.IntegerField()
