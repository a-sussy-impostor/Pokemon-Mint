# from battle import *
from pokemon import *
from map import *
import random

# Initialize game variables
player = None
located = None
wild_pokemon = None
direction = None
encounter_probability = random.uniform(0.03,0.2)
# Define game classes
class Player:
    def __init__(self, name, pokemon):
        self.name = name # str
        self.pokemon = pokemon # array
        self.money = 10000 # int
class Location:
    def __init__(self, name, description, wild, map):
        self.name = name
        self.description = description
        self.pokemon = wild # Wild Pokemon Array
        self.map = map # The Whole Enviroment Overview Of The Location

# Define game functions
def new_game():
    # Initialize player
    name = input(f"Welcome to the world of {red}Pokemon{reset}! What is your name? \n Name: ")
    if name == "":
        name = "Player"
    rivalName = input("What is your rival's name? \n Name: ")
    if rivalName == "":
        
    global player
    player = Player(name, [])
    print("Welcome, " + player.name + "!")
    # Initialize game world
    global current_location
    current_location = Location("Marusha Town", f"A small town where {player.name}'s home and {rivalName}'s home located in.",)
    # Start game loop
    game_loop()

def game_loop():
    while True:
        # Check for wild Pokémon encounters
        global wild_pokemon
        if random.random() < encounter_probability:
            wild_pokemon = 
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
