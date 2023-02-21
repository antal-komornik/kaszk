from django.shortcuts import render, redirect
from . models import News
from . form import NewsForm
# Create your views here.


def Home(requset):
    news = News.objects.all()
    return render(requset, "index.html", {"news": news})


def newNews(request):
    if request.method == "GET":
        form = NewsForm()
        return render(request, "newNews.html", {"form": form})
    elif request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
