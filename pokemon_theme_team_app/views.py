from django.shortcuts import render
from .models import Pokemon
# Create your views here.
# my_pokemon = Pokemon()

def index(request):
  return render(request, "pages/index.html")

def team(request):
  Pokemon.getMon()
  return render(request, "pages/team.html")