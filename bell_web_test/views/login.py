from django.shortcuts import render
from bell_web_test.forms.login.loginForm import LoginForm
from django.contrib.auth import authenticate, login


def index(request):
    """
    認証画面
    :param request:
    :return:
    """
    form = LoginForm(request.POST or None)
    if form.is_valid():
        loginid = form.data["loginid"]
        user = authenticate(loginid=loginid, password=form.data["password"])
        if user:
            login(request, user)

    return render(request, "login/index.html", {"form": form})
