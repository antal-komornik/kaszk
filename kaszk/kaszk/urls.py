from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("newNews/", views.newNews, name="newnews"),
    path("new/", views.NewsKAC, name="newskac"),

]
