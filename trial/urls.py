#from django.conf.urls import url
from django.urls import path
from .views import (
    login_view, register_view, logout_view, index_view, personal_information_view
)




urlpatterns = [
    path("index/", index_view, name="index"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("personal_information", personal_information_view, name="personal information"),

]
