from bell_app.forms.commonForm import CommonForm
from django import forms

from v1.models import Article
from django_summernote.widgets import SummernoteWidget


class StampShowForm(CommonForm):
    """
    記事一覧画面用Form
    """
    test = "test"


