from django.contrib import admin
from django.urls import path

from main import views

urlpatterns = [
    path('', views.weather, name='weather'),
    path('github', views.github, name='github'),
    path('linkedin', views.linkedin, name='linkedin')
]
