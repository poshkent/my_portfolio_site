from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Jamboard, File, Image
from django.shortcuts import get_object_or_404


def home(request):
    jamboards = None
    if request.method == 'POST':
        try:
            jamboard = Jamboard.objects.get(Q(title=request.POST['search']))
            return redirect('jamboard', jamboard_id=jamboard.id)
        except Jamboard.DoesNotExist:
            error = 'No results found'
            return render(request, 'jamboard/home.html', {'jamboards': jamboards, 'error': error})
    else:
        if request.user.is_authenticated:
            jamboards = Jamboard.objects.filter(
                Q(author=request.user.username))
        return render(request, 'jamboard/home.html', {'jamboards': jamboards})


def new(request):
    if (request.user.is_anonymous):
        return redirect('/auth/login/?next=/jamboard/new')
    if request.method == 'POST':
        if request.POST['title']:
            try:
                Jamboard.objects.get(title=request.POST['title'])
                return render(request, 'jamboard/new.html', {'error': 'Title already exists.'})
            except Jamboard.DoesNotExist:
                jamboard = Jamboard()
                jamboard.title = request.POST['title']
                jamboard.author = request.user.username
                jamboard.save()
                return redirect('jamboard', jamboard_id=jamboard.id)
        else:
            return render(request, 'jamboard/new.html', {'error': 'All fields are required.'})
    return render(request, 'jamboard/new.html')


def jamboard(request, jamboard_id):
    if request.method == 'POST':
        board = get_object_or_404(Jamboard, id=jamboard_id)
        if 'title' in request.POST:
            try:
                Jamboard.objects.get(title=request.POST['title'])
            except Jamboard.DoesNotExist:
                board.title = request.POST['title']
                board.save()
        elif 'text' in request.POST:
            board.text = request.POST['text']
            board.save()
        elif 'file' in request.FILES:
            file = File()
            file.file = request.FILES['file']
            file.jamboard = board
            file.save()
        elif 'image' in request.FILES:
            image = Image()
            image.image = request.FILES['image']
            image.jamboard = board
            image.save()
        elif 'del_pic' in request.POST:
            for key in request.POST:
                if 'delete' in key:
                    file = get_object_or_404(Image, id=request.POST[key])
                    file.delete()
        elif 'del_file' in request.POST:
            for key in request.POST:
                if 'delete' in key:
                    file = get_object_or_404(File, id=request.POST[key])
                    file.delete()
        return redirect('jamboard', jamboard_id=jamboard_id)

    board = get_object_or_404(Jamboard, id=jamboard_id)
    images = list(board.images.all())
    files = list(board.files.all())
    for file in files:
        file.name = file.file.name.split('/')[-1]
        
    return render(request, 'jamboard/jamboard.html', {'board': board, 'files': files, 'images': images})
