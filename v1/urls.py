from django.conf.urls import url, include
from django.urls import  path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from v1.views.article import ArticleView
from v1.views.article_detail import ArticleDetailView
from v1.views.stamp import StampView
from v1.views.token import TokenView

router = routers.SimpleRouter()
urlpatterns = [
    path("auth/token", obtain_jwt_token),
    path("auth/token/verify", verify_jwt_token),
    path('auth/token/refresh', refresh_jwt_token),
    path('article', ArticleView.as_view()),
    path('article_detail', ArticleDetailView.as_view()),
    path('stamp', StampView.as_view()),
    path('token', TokenView.as_view()),
]

urlpatterns += router.urls