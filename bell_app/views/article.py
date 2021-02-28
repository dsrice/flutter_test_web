from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from bell_app.forms.article.articleForm import ArticleIndexForm, ArticleNewForm, ArticleEditForm
from v1.models import Article


@login_required
def index(request):
    """
    記事一覧画面
    :param request
    :return:
    """
    form = ArticleIndexForm()

    context = {"title": "記事一覧", "form": form}
    return render(request, "article/index.html", context)


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


@login_required
def create(request):
    """
    記事の新規登録
    :param request
    :return:
    """
    form = ArticleNewForm(request.POST or None)
    if form.is_valid():
        article = Article()
        article.title = form.cleaned_data["article_title"]
        article.body = form.cleaned_data["article_body"]

        article.save(request)

        return redirect("bell_app:article_index")

    return redirect("bell_app:article_new")


@login_required
def edit(request, article_id):
    """
    記事作成画面
    :param article_id:
    :param request
    :return:
    """
    if request.POST:
        form = ArticleEditForm(request.POST)
        print("test")
        if form.is_valid():
            article = Article.objects.get(id=article_id)
            article.title = form.cleaned_data["article_title"]
            article.body = form.cleaned_data["article_body"]

            article.save(request)

            return redirect("bell_app:article_index")
    else:
        form = ArticleEditForm(None)
        form.set_init(request, article_id)

    context = {"title": "記事編集", "form": form}
    return render(request, "article/edit.html", context)
