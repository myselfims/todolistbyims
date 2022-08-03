from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.loginpage),
    path('login/',views.loginn),
    path('signup/',views.signup),
    path('logout/',views.user_logout),
    path('home/',views.home),
    path('search/',views.search)
]