from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.home),
    path('home', views.home),
    path('specialists', views.specialists),
    path('contact', views.contact),
    path('appointment', views.appointment),
]
