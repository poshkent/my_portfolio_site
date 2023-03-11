from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Jamboard, File, Image
from django.shortcuts import get_object_or_404


# Create your views here.

def home(request):
    jamboards = None
    if request.user.is_authenticated:
        jamboards = Jamboard.objects.filter(Q(author=request.user.username))
    return render(request, 'jamboard/home.html', {'jamboards': jamboards})

def new(request):
    if (request.user.is_anonymous):
        return redirect('/auth/login/?next=/jamboard/new')
    if request.method == 'POST':
        if request.POST['title']:
            jamboard = Jamboard()
            jamboard.title = request.POST['title']
            jamboard.author = request.user.username
            jamboard.save()
            return redirect('jamboard', conversation_id=jamboard.id)
        else:
            return render(request, 'jamboard/new.html', {'error': 'All fields are required.'})
    return render(request, 'jamboard/new.html')

def jamboard(request, conversation_id):
    board = get_object_or_404(Jamboard, id=conversation_id)
    images = list(board.images.all())
    files = list(board.files.all())
    return render(request, 'jamboard/jamboard.html', {'board': board, 'files': files, 'images': images})