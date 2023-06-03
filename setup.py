pokemons = []

import random

# Initialize game variables
player = None
current_location = None
wild_pokemon = None
direction = None
encounter_probability = 0.1
# Define game classes
class Player:
    def __init__(self, name, pokemon):
        self.name = name
        self.pokemon = pokemon
        self.money = 0
class Location:
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits
