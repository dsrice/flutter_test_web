from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from bell_app.forms.stamp.stampForm import StampShowForm, StampDetailForm
from v1.models import StampRecord, User
from v1.models.stamp_total import StampTotal
from django.core.paginator import Paginator

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
    num = 1
    if request.POST:
        form = StampDetailForm(request.POST)
        if form.data["stamp_count"]:
            stamp = StampRecord()
            stamp.user = StampTotal.objects.get(id=id).user
            stamp.stamp = form.data["stamp_count"]
            print(id)
            print(stamp)
            stamp.save(request)
            num = 1

    elif request.GET:
        print("GET")
        num = request.GET.get('p')
        if not num:
            num = 1
        print(num)

    form = StampDetailForm()
    form.user = StampTotal.objects.get(id=id)
    records = StampRecord.objects.filter(user=form.user.user).order_by("-id")
    paginator = Paginator(records, 10)
    form.records = paginator.get_page(num)
    form.page_obj = paginator
    context = {"title": "スタンプ履歴", "form": form}
    return render(request, "stamp/detail.html", context)
