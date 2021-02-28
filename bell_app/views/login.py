from django.shortcuts import render, redirect
from bell_app.forms.login.loginForm import LoginForm
from django.contrib.auth import authenticate, login


def index(request):
    """
    認証画面
    :param request:
    :return:
    """
    print("login")
    form = LoginForm(request.POST or None)
    if form.is_valid():
        loginid = form.data["loginid"]
        user = authenticate(loginid=loginid, password=form.data["password"])
        if user:
            login(request, user)
            return redirect("bell_app:article_index")

    return render(request, "login/index.html", {"form": form})
