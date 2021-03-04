from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from bell_app.forms.stamp.stampForm import StampShowForm
from v1.models.stamp_total import StampTotal


@login_required
def show(request):
    """
    スタンプ需要協一覧画面
    :param request
    :return:
    """
    form = StampShowForm()
    userlist = StampTotal.objects.all()
    form.userlist = userlist

    context = {"title": "スタンプ管理", "form": form}
    return render(request, "stamp/show.html", context)


@login_required
def detail(request, id):
    """
    スタンプ利用履歴画面
    :param request
    :return:
    """
    form = StampShowForm()

    context = {"title": "スタンプ履歴", "form": form}
    return render(request, "stamp/detail.html", context)
