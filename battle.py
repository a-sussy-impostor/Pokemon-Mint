from starters import *
from battlecmd import battle
print("--- Welcome to a Pokémon Battle! ---")
print("You've encountered a wild Charmander!")
# Initialize the Pokémon

# player_pkmn = Pikachu()
player_pkmn = pokemons[0]
wild_pkmn = Charmander()
# Pokémon introduction
print("Go, " + player_pkmn.name + "!")
print("Wild " + wild_pkmn.name + " appeared!")
# Loop through battle rounds until a Pokémon faints
while True:
    # Player turn
    print("--- Your turn ---")
    player_move = input("Enter your move: ")
    player_pkmn.attack(wild_pkmn, player_move)
    if wild_pkmn.hp <= 0:
        # print("You defeated " + wild_pkmn.name + "! Congrats!")
        battle("complete")
        break
    # Wild Pokémon turn
    print("--- Wild " + wild_pkmn.name + "'s turn ---")
    wild_pkmn.attack(player_pkmn)
    if player_pkmn.hp <= 0:
        # print("Oh no! Your " + player_pkmn.name + " fainted!")
        battle("fail")
        break



