from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
      
urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.Home, name="home"),
    path("newNews/", views.newNews, name="newnews"),
<<<<<<< HEAD
    path("newskac/", views.NewsKAC, name="newskac"),
    path("newsmszk/", views.NewsMSZK, name="newsmszk"),
    path("newspkszk/", views.NewsPKSZK, name="newspkszk"),
    path("newsgtszk/", views.NewsGTSZK, name="newsgtszk"),
=======
    path("news/", views.KACnews, name="kacnews"),
    path("news/", views.GTSZKnews, name="gtszknews"),
    path("news/", views.MSZKnews, name="mszknews"),
    path("news/", views.PKSZKnews, name="pkszknews"),
>>>>>>> 0e5d860592bf245766994e79abba4aec279fa0bf
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)