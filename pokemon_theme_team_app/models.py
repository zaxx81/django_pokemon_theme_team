from django.db import models
import requests, pprint

# Create your models here.
class Pokemon(models.Model):
  pokemon_count = 0
  pokemon_caught = []

  def __init__(self, id, name, types, sprites) -> None:
    self.id = id
    self.name = name
    self.types = types
    self.sprites = sprites

  def getMon():
    pp = pprint.PrettyPrinter(indent=2, depth=2)
    pokemon_endpoint = 'https://pokeapi.co/api/v2/pokemon'
    types_endpoint = 'https://pokeapi.co/api/v2/type/'
    
    # Determine the count for pokemon(endpoint)
    limit = '?limit=1'
    pokemon_url = pokemon_endpoint+limit
    response = requests.get(pokemon_url)
    responseJSON = response.json()
    # pp.pprint(responseJSON['count'])
    Pokemon.pokemon_count = int(responseJSON['count'])
    print(Pokemon.pokemon_count)

    # Testing Hardcoded Getting Pikachu
    # Get a pokemon(type) from pokemon(endpoint)
    pokemon_url = pokemon_endpoint + '/25'
    response = requests.get(pokemon_url)
    responseJSON = response.json()
    # pp.pprint(responseJSON)
    print(responseJSON['id'])
    print(responseJSON['name'])
