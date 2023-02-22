from django.shortcuts import render, redirect
from . models import News
from . form import NewsForm
# Create your views here.


def Home(requset):
    return render(requset, "index.html")


def newNews(request):
    if request.method == "GET":
        form = NewsForm()
        return render(request, "newNews.html", {"form": form})
    elif request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")


def NewsKAC(request):
    news = News.objects.all().filter(News.group == "KAC")
    return render(request, "index.html", {"news": news})
