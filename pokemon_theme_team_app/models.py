from django.db import models
import requests
import random

# Create your models here.
class Pokemon():
    pokemon_count = 0
    pokemon_data = []
    pokemon_caught = []
    pokemon_endpoint = 'https://pokeapi.co/api/v2/pokemon'
    types_endpoint = 'https://pokeapi.co/api/v2/type/'

    def __init__(self, mon_id, name, types, sprites) -> None:
        self.id = mon_id
        self.name = name
        self.types = types
        self.sprites = sprites
    
    ## Class Methods        
    # Determine the count for pokemon(endpoint)
    def getPokemonCount():
        query_strings = {
            'limit': '1'
        }
        response = requests.get(Pokemon.pokemon_endpoint, params=query_strings)
        responseJSON = response.json()
        Pokemon.pokemon_count = int(responseJSON['count'])

    
    # Get all pokemon(types) from pokemon(endpoint)
    def getPokemonData():
        query_strings = {
            'limit': Pokemon.pokemon_count
        }
        response = requests.get(Pokemon.pokemon_endpoint, params=query_strings)
        responseJSON = response.json()
        Pokemon.pokemon_data = responseJSON['results']


    # Get a pokemon(type) from pokemon(endpoint) @ url
    # Create a Pokemon instance and append to Pokemon.pokemon_caught[]
    def getPokemon(pokemon_url):
        response = requests.get(pokemon_url)
        responseJSON = response.json()

        species_name = responseJSON['species']['name']
        # Uppercase first letter for name
        name = species_name[0].upper() + species_name[1:]
        
        Pokemon.pokemon_caught.append( 
            Pokemon(
                responseJSON['id'],
                name,
                responseJSON['types'],
                responseJSON['sprites']
            )
        )


    # Get a random() pokemon(type) from pokemon(endpoint)
    def getRandomMon():
        random_index = random.randint(0, Pokemon.pokemon_count)
        pokemon_url = Pokemon.pokemon_data[random_index]['url']
        Pokemon.getPokemon(pokemon_url)


    # Get a team of five Pokemon with arg:types
    def getTeam(types):
        pokemon_pool = []

        # Iterates each pokemon type in args:type
        for pokemon_type in types:
            # Requests a type(type) from types(endpoint)
            types_url = pokemon_type['type']['url']
            response = requests.get(types_url)
            response_JSON = response.json()

            # Adds all the pokemon (*API Pokemon includes name and url)
            # of that type(type) to pokemon_pool[]
            for pokemon in response_JSON['pokemon']:
                pokemon_pool.append(pokemon['pokemon'])

        # Append 5 random pokemon from pokemon_pool[]
        for i in range(5):
            random_index = random.randint(0, len(pokemon_pool) - 1)
            random_pokemon = pokemon_pool[random_index]
            print(f"Caught a pokemon '{random_pokemon['name']}'")
            Pokemon.getPokemon(random_pokemon['url'])
            

    # Clears the Pokemon.pokemon_caugh:list[Pokemon]
    def clearPokemonCaught():
        Pokemon.pokemon_caught = []


    # Runs all the class methods to get a Pokemon Team
    def getMon():
        Pokemon.clearPokemonCaught()
        Pokemon.getPokemonCount()
        Pokemon.getPokemonData()
        Pokemon.getRandomMon()
        Pokemon.getTeam(Pokemon.pokemon_caught[0].types)