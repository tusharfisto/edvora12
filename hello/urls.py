from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf.urls import handler404
from django.views.static import serve

from django.conf.urls.static import static

from . import views

app_name = "hello"

urlpatterns = [
    path("",views.index, name="index"),
    path("register", views.register, name="register"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("terminate",views.terminate,name="terminate"),
    path("forgot",views.forgot,name="forgot"),
    path("reset",views.reset,name="forgot")
    # path("login", views.ups, name="ups")

]
