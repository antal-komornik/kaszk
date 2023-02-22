from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("newNews/", views.newNews, name="newnews"),
    path("news/", views.KACnews, name="kacnews"),
    path("news/", views.GTSZKnews, name="gtszknews"),
    path("news/", views.MSZKnews, name="mszknews"),
    path("news/", views.PKSZKnews, name="pkszknews"),
]
