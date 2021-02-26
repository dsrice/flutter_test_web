from bell_app.forms.commonForm import CommonForm
from django import forms

class ArticleIndexForm(CommonForm):
    title = forms.CharField()