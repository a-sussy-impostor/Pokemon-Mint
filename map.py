from colours import *
import random 

groundMap = f"""
                        Secret Base - - - - {cyan}Northern Tower{reset} - - - {red}Reiltas Ruins{reset}
                                                          |
               {blue}Dabirc City{reset} - {yellow}Nellight Town{reset} - - - - - {green}Reiltas Town{reset}                     
                       |                      |        \                                                                                      {yellow}Marusha Town{reset}
                        \                 Fallen Cave    \ - - - - {red}Mt. Foxclore{reset} - - - - - {blue}Vasagle City{reset}                         (1001) 
                         (                                                                                      (1015)                                 (1002)
                          \                                                                                      /                                       /
{purple}Underground Entrace{reset}   -   -   -  {blue}Bronea City{reset} - - {yellow}Skaxis City{reset} - - - {green}Mt. Crimson{reset} - - - - {yellow}Feandra City{reset}
                                                         |                                                                                           (1003)
                                                         |                                {red}Power Plant{reset}                                       |
                                                          \                                           |                                                
                                                {cyan}Ancient Tower{reset} - {green}Loodon Village{reset} - {red}Dawn Fortress{reset}      {blue}Silek City{reset}
"""

# t means tiles

empty_t = "#"
road_t = brown + "$" + reset
bush_t = green + "§" + reset
sea_t = cyan + "/" + reset
wall_t = dark + "X" + reset

pokecenter_t = red + "P" + reset
pokemart_t = blue + "M" + reset
building_t = lime + "○" + reset

loot_t =  pink + "?" + reset
loot_b_t = yellow + "!" + reset

exit_n_t = purple + "↑" + reset
exit_s_t = purple + "↓" + reset
exit_w_t = purple + "←" + reset
exit_e_t = purple + "→" + reset

raid_t = bold + red + "▲" + reset

def init_raid(area, chance = random.uniform(0.0101,0.0499): # towns/cities/dungeons/towers/entraces dont have raid
  global raid_t
  area_new = area
  for r in range(len(area)):
    raid_bool = random.random() < chance
    if raid_bool:
      if area_new[r] in [exit_n_t,exit_s_t,exit_e_t,exit_w_t]
        continue
      area_new[r] = raid_t
  return area_new

marusha = [
wall_t,wall_t,wall_t,wall_t,exit_n,exit_n,wall_t,wall_t
pokecenter
