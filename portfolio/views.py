from django.shortcuts import render, redirect
from portfolio.models import Project
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'portfolio/main.html', context=None)


def pictures(request):
    return render(request, 'portfolio/pictures.html', context=None)


def projects(request):
    if 'skill' in request.GET:
        option = request.GET['skill']
        projects = Project.objects.all()
        for proj in projects:
            if not option.lower() in proj.skills.lower():
                projects = projects.exclude(id=proj.id)
    else:
        projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})


def details(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'portfolio/details.html', {'project': project})


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)