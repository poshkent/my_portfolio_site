from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'jamboard/home.html')

def new(request):
    return render(request, 'jamboard/new.html')

def jamboard(request, conversation_id):
    return render(request, 'jamboard/jamboard.html')