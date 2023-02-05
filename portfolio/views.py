from django.shortcuts import render, redirect


def index(request):
    return render(request, 'portfolio/main.html', context=None)

def pictures(request):
    return render(request, 'portfolio/pictures.html', context=None)