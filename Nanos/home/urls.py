from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("resume", views.resume, name='resume'),
    path("services", views.services, name='services'),
    path("working", views.working, name='working'),
    path("contact", views.contact, name='contact'), 
]