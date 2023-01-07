from django.contrib import admin 
from django.urls import path, include 
from . import views 
from django.shortcuts import render, HttpResponse

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.profile),
    path('kyc/', views.get_finance_info), 
    path('home/', views.home)
]

