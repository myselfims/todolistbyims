from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.loginpage),
    path('login/',views.login),
    path('signup/',views.signup),
    path('logout/',views.logout),
    path('home/',views.home),
    path('search/',views.search)
]