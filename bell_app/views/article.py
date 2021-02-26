from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse


@login_required
def index(request):
    """
    記事一覧画面
    :param request
    :return:
    """

    return render(request, "article/index.html")


