from bell_app.forms.commonForm import CommonForm
from django import forms

from v1.models import Article
from django_summernote.widgets import SummernoteWidget


class ArticleIndexForm(CommonForm):
    """
    記事一覧画面用Form
    """
    article_title = forms.CharField()

    def __init__(self, text):
        self.title = text


class ArticleNewForm(forms.Form):
    """
    記事作成画面Form
    """
    article_title = forms.CharField(label="タイトル", max_length=100)
    article_body = forms.CharField(widget=SummernoteWidget())

