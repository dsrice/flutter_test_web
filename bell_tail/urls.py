from django.urls import path
from bell_tail.views import login

urlpatterns = [
    path("login/", login.index, name="login"),
]