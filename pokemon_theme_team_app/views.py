from django.shortcuts import render
from .models import Pokemon
# Create your views here.
# my_pokemon = Pokemon()

def index(request):
  return render(request, "pages/index.html")

def team(request):
  Pokemon.getMon()
  pokemon_list = Pokemon.pokemon_caught
  my_data = {
    "pokemons": pokemon_list,
  }
  # print(my_data['pokemon_caught'][0].name)
  return render(request, "pages/team.html", my_data)