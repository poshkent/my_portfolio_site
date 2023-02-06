from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def account(request):
    if (request.method == "POST"):
        user = User.objects.get(username=request.user)
        if (request.POST.get('email') != user.email):
            user.email = request.POST.get('email')
        if (request.POST.get('first_name') != user.first_name):
            user.first_name = request.POST.get('first_name')
        if (request.POST.get('last_name') != user.last_name):
            user.last_name = request.POST.get('last_name')
        user.save()
        return redirect('/auth/account')
    return render(request, "users/account.html")