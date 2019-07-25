from django.conf.urls import url

from django.urls import path
from .views import (
    login_view, register_view, logout_view, index_view, resume_form
)




urlpatterns = [
    path("index/", index_view, name="index"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("personal_information", resume_form, name="personal information"),

]
