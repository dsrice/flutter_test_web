from bell_app.forms.commonForm import CommonForm
from django import forms

from v1.models import Article
from django_summernote.widgets import SummernoteWidget


class ArticleIndexForm(CommonForm):
    """
    記事一覧画面用Form
    """
    article_title = forms.CharField()
    articles = Article.objects.all().order_by("-id")


class ArticleNewForm(forms.Form):
    """
    記事作成画面Form
    """
    article_title = forms.CharField(label="タイトル", max_length=100)
    article_body = forms.CharField(widget=SummernoteWidget())


class ArticleEditForm(forms.Form):
    """
    記事編集画面Form
    """
    article_title = forms.CharField(label="タイトル", max_length=100)
    article_body = forms.CharField(widget=SummernoteWidget())

    def set_init(self, request, article_id):
        """
        初期化
        :param request:
        :param article_id:
        :return:
        """
        super(ArticleEditForm, self).__init__()
        article = Article.objects.get(id=article_id)
        self.fields["article_title"].initial = article.title
        self.fields["article_body"].initial = article.body
