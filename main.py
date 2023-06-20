# from battle import *
from pokemon import *

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

# Define game functions
def new_game():
    # Initialize player
    name = input("What is your name? ")
    global player
    player = Player(name, pokemon)
    print("Welcome, " + player.name + "!")
    # Initialize game world
    global current_location
    current_location = Location("Pallet Town", "You are in a small town with a few houses and a lab to the north.", {"north": "Lab"})
    # Start game loop
    game_loop()
def game_loop():
    while True:
        # Handle event
        # Check for wild Pokémon encounters
        global wild_pokemon
        if random.random() < encounter_probability:
            wild_pokemon = Charmander()
            print("A wild " + wild_pokemon.name + " appeared!")
        # Render game world
        render_world()
        # Update display
        clock.tick(60)

def render_world():
    # Draw current location
    print(current_location.name, 100)
    # Draw location description
    print(current_location.description, 150)
    # Draw wild Pokémon if encountered
    if wild_pokemon:
        print("A wild " + wild_pokemon.name + " appeared!", 200)

# Start new game
new_game()
