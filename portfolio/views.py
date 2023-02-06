from django.shortcuts import render, redirect
from portfolio.models import Project
from django.db.models import Avg, Count, Q


def index(request):
    return render(request, 'portfolio/main.html', context=None)


def pictures(request):
    return render(request, 'portfolio/pictures.html', context=None)


def projects(request):
    if 'skill' in request.GET:
        option = request.GET['skill']
        projects = Project.objects.filter(Q(skills__icontains=option))
    else:
        projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})


def details(request, id):
    try:
        project = Project.objects.get(id=id)
    except Project.DoesNotExist:
        return redirect('projects')
    return render(request, 'portfolio/details.html', {'project': project})
