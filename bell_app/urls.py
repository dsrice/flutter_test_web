from django.urls import path
from bell_app.views import login, article

app_name = 'bell_app'
urlpatterns = [
    path("login/", login.index, name="login"),
    path("article/", article.index, name="article_index"),
    path("article/new", article.new, name="article_new"),
    path("article/create", article.create, name="article_create"),
]