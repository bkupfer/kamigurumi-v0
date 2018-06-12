from django.shortcuts import render, redirect
from .models import Kamigurumi


def home(request):
    return render(request, "index.html", {})


def contact_us(request):
    return render(request, "contact.html", {})


def about_us(request):
    return render(request, "about.html", {})


def item_detail(request):
    if request.GET:
        kamigurumi_id = request.GET.get("id", None)
        kamigurumi = Kamigurumi.objects.filter(id=kamigurumi_id)
        if kamigurumi:
            return render(request, "item_detail.html", {"kamigurumi": kamigurumi.first()})
    return redirect("home")


def news(request):
    return render(request, "news.html", {})

