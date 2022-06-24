# pokemon_theme_team_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("team/", views.team, name="team"),
]