from django.contrib import admin
from django.urls import path
from finder import views
urlpatterns = [
    path('', views.findhotels, name="findhotels"),
]
