from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    記事一覧画面
    :param request
    :return:
    """

    return render(request, "article/index.html")


def new(request):
    """
    記事作成画面
    :param request:
    :return:
    """

    return render(request, "article/index.html")

