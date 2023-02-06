from django.urls import path
from portfolio import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('hobbies/', views.pictures, name='pictures'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>/', views.details, name='details'),
]