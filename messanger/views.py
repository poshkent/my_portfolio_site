from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Conversation, Message
from django.db.models import Avg, Count, Q
from django.http import JsonResponse

# Create your views here.


def home(request):
    if (request.user.is_anonymous):
        return redirect('/auth/login/?next=/messanger/')
    user = User.objects.get(username=request.user)
    conversations = Conversation.objects.filter(Q(user1=user) | Q(user2=user))
    return render(request, 'messanger/home.html', {'conversations': conversations})


def conversation(request, conversation_id):
    if (request.user.is_anonymous):
        return redirect('/auth/login/?next=/messanger/')
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        conversation = Conversation.objects.get(id=conversation_id)
        message = Message.objects.create(
            conversation=conversation, author=user.username, text=request.POST['text'])
        return redirect('/messanger/conversation/' + str(conversation.id))
    user = User.objects.get(username=request.user)
    conversation = Conversation.objects.get(id=conversation_id)
    messages = conversation.messages.all()
    print(messages)
    return render(request, 'messanger/conversation.html', {'conversation': conversation, 'messages': messages})


def new(request):
    if (request.user.is_anonymous):
        return redirect('/auth/login/?next=/messanger/')
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        user2 = User.objects.get(username=request.POST['username'])
        conversation = Conversation.objects.create(
            user1=user, user2=user2, name=user.username + " " + user2.username)
        return redirect('/messanger/conversation/' + str(conversation.id))
    return render(request, 'messanger/new.html')


def get_users(request):
    if (request.user.is_anonymous):
        return redirect('/auth/login/?next=/messanger/')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        username = request.GET.get('username', None)
        users = list(User.objects.filter(Q(username__icontains=username)))
        users = users[:5]
        results = []
        if username:
            if users:
                for user in users:
                    results.append(user.username)
            else:
                results = ['No users found']
        else :
            results = ['Type something']
        return JsonResponse(results, safe=False)
    else:
        return render(request, 'messanger/new.html')
