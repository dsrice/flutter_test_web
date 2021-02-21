from django.conf.urls import url, include
from django.urls import  path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

router = routers.SimpleRouter()
urlpatterns = [
    path("auth/token", obtain_jwt_token),
    path("auth/token/verify", verify_jwt_token),
    path('auth/token/refresh', refresh_jwt_token),
]

urlpatterns += router.urls