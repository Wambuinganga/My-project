from django.urls import path
from .views import register_user, login, user_update


urlpatterns=[
path("register/", register_user, name="register_user"),
path("login/", login, name="login"),
path("update/", user_update, name="update")
]