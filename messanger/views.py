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
    if request.method == 'POST' and request.POST['text']:
        user = User.objects.get(username=request.user)
        conversation = Conversation.objects.get(id=conversation_id)
        Message.objects.create(
            conversation=conversation, author=user.username, text=request.POST['text'])

        lang_ref = request.META.get('HTTP_REFERER').split('/')[-5]
        print(lang_ref)
        return redirect(f'/{lang_ref}/messanger/conversation/' + str(conversation.id))


    try:
        conversation = Conversation.objects.get(id=conversation_id)
    except Conversation.DoesNotExist:
        return redirect('/messanger/')
    if (request.user.username in [conversation.user1, conversation.user2]):
        messages = list(conversation.messages.all())
    else:
        return render(request, 'messanger/conversation.html', {'error': 'You are not a member of this conversation'})
    if messages:
        last_message_id = messages[-1].id
    else:
        last_message_id = 0
    return render(request, 'messanger/conversation.html', {'conversation': conversation, 'messages': messages, 'last_message_id': last_message_id})


def new(request):
    if (request.user.is_anonymous):
        return redirect('/auth/login/?next=/messanger/')
    if request.method == 'POST':
        user = User.objects.get(username=request.user)
        try:
            user2 = User.objects.get(username=request.POST['username'])
            conversation = Conversation.objects.get(
                Q(user1=user, user2=user2) | Q(user1=user2, user2=user))
        except User.DoesNotExist:
            return render(request, 'messanger/new.html', {'error': 'User not found'})
        except Conversation.DoesNotExist:
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
        else:
            results = ['Type something']
        return JsonResponse(results, safe=False)
    else:
        return render(request, 'messanger/new.html')


def get_last_message_id(request):
    if (request.user.is_anonymous):
        return redirect('/auth/login/?next=/messanger/')
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        conversation_id = request.POST.get('conversation_id', None)
        print(conversation_id)
        conversation = Conversation.objects.get(id=conversation_id)
        messages = list(conversation.messages.all())
        if messages:
            last_message_id = messages[-1].id
        else:
            last_message_id = 0
        return JsonResponse(last_message_id, safe=False)
    else:
        return render(request, 'messanger/conversation.html')
