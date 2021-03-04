from django.urls import path
from bell_app.views import login, article, stamp

app_name = 'bell_app'
urlpatterns = [
    path("login/", login.index, name="login"),
    path("article/", article.index, name="article_index"),
    path("article/new", article.new, name="article_new"),
    path("article/create", article.create, name="article_create"),
    path("article/<int:article_id>/edit", article.edit, name="article_edit"),
    path("stamp/", stamp.show, name="stamp_show"),
    path("stamp/<int:id>/detail", stamp.detail, name="stamp_detail"),
]