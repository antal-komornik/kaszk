from django.shortcuts import render

# Create your views here.


def Home(requset):
    return render(requset, "index.html")
