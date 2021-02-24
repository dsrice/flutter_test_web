from django.urls import path
from bell_web_test.views import login, article

urlpatterns = [
    path("login/", login.index, name="login"),
    path("article/", article.index, name="article_index")
]