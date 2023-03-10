from django.contrib.auth.views import LogoutView 
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("account/", views.account, name="account"),
] 