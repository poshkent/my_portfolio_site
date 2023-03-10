"""portfolio_azure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView 
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.home, name="messanger_home"),
    path('new/', views.new, name='new'),
    path('conversation/<int:conversation_id>/', views.conversation, name='conversation'),
    path('get_users/', views.get_users, name='get_users'),
    path('get_last_message/', views.get_last_message_id, name='get_last_message_id'),
]


