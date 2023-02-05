from django.urls import path
from portfolio import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('hobbies/', views.pictures, name='pictures'),
]