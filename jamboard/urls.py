from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView 
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="jamboard_home"),
    path('new/', views.new, name='new_jamboard'),
    path('<int:jamboard_id>/', views.jamboard, name='jamboard'),
    # path('get_users/', views.get_users, name='get_users'),
    # path('get_last_message/', views.get_last_message_id, name='get_last_message_id'), # type: ignore
]