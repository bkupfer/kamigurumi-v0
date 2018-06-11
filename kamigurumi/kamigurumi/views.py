from django.shortcuts import render


def home(request):
    return render(request, "index.html", {})


def contact_us(request):
    return render(request, "contact.html", {})


def about_us(request):
    return render(request, "about.html", {})


def item_detail(request):
    return render(request, "item_detail.html", {})


def news(request):
    return render(request, "news.html", {})



