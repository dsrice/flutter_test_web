from django.urls import path
from bell_web.views import login

urlpatterns = [
    path("login/", login.index, name="login")
]