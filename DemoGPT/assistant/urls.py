from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gpt/', views.query_view, name='gpt'),
    path('rev/', views.rev_search, name='rev')
]