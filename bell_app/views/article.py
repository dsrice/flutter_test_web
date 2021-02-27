from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from bell_app.forms.article.articleForm import ArticleIndexForm, ArticleNewForm


@login_required
def index(request):
    """
    記事一覧画面
    :param request
    :return:
    """
    form = ArticleIndexForm("記事一覧")

    return render(request, "article/index.html", {"form": form})

@login_required
def new(request):
    """
    記事作成画面
    :param request
    :return:
    """
    form = ArticleNewForm()

    context = {"title": "記事作成", "form": form}
    return render(request, "article/new.html", context)
