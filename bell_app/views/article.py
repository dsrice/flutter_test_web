from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from bell_app.forms.article.articleForm import ArticleIndexForm

@login_required
def index(request):
    """
    記事一覧画面
    :param request
    :return:
    """
    form = ArticleIndexForm("記事一覧")

    return render(request, "article/index.html", {"form": form})


