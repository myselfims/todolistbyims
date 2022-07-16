from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('home/',views.home),
    path('search/',views.search)
]