from bell_app.forms.commonForm import CommonForm
from django import forms


class ArticleIndexForm(CommonForm):
    article_title = forms.CharField()

    def __init__(self, text):
        self.title = text
