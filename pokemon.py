
class Pokemon:
    def __init__(self, name, type, alt, halt, moves, hp, atk, df, spa, spd, spe, nml, nm, level):
        self.name = name # name
        self.type = type # type
        self.alt = alt # ability
        self.halt = halt #hidden abillity
        self.moves = moves #moves
        self.level = level 
        sl = self.level - 1
        self.hp = hp + sl *2
        self.atk = atk + sl * 2
        self.df = df + sl * 2
        self.spa = spa + sl * 2
        self.spd = spd + sl * 2
        self.spe = spe + sl * 2
        self.exp = 0
        self.next_level_exp = 100 * (2 ** (self.level - 1))
    def checkType(type, enemy):
      if type == enemy.type:
        pass
    def attack(self, enemy, move):
        if move >= len(self.moves) - 1 or move < 1:
            print("That move number doesn't exist!")
        else:
            dmg = self.moves[move][0]
            enemy.hp -= dmg * self.checkType()
            print(self.name + " used " + move + "! " + enemy.name + " took " + str(dmg) + " damage.")
            print(enemy.name + "'s HP is now " + str(enemy.hp))
        if enemy.hp == 0:
            print(enemy.name + " fainted!")
            self.gain_exp(50)
    def gain_exp(self, exp):
        self.exp += exp
        if self.exp >= self.next_level_exp:
            self.level_up()
    def level_up(self):
        self.level += 1
        self.exp = 0
        self.next_level_exp = self.next_level_exp * 2
        self.hp = self.hp + 2 
        self.atk = self.atk + 2
        self.df = self.df + 2
        self.spa = self.spa + 2
        self.spd = self.spd + 2
        self.spe = self.spe + 2
        print(self.name + " leveled up!")
        print("New level: " + str(self.level))
        print("New HP: " + str(self.hp))
        print("New ATK: " + str(self.hp))
        if self.level in self.nm.keys():
          self.moves[self.nm.keys()[self.nml.index(self.level)]] = self.nm.values()[self.nml.index(self.level)]

class Mossprout(Pokemon):
    def __init__(self):
        moves = {
            "Scratch": [30,"Normal",0,20,100,[None],"Use claws or hands to attack."],
        }
        new_moves = {
            # Move Name: Damage, Type, Kind, PP, Accuracy, Special Effects
            # Kinds: 0 --> Physical ; 1 --> Special ; 2 --> Other
            # Accuracy 0 --> Can't Miss
            "Leafage": [40,"Grass",0,40,100,[None],"Use leaves to attack."],
            "Tackle": [40,"Normal",0,30,100,[None],"Use body to hit and attack."],
            "Growl": [0,"Normal",2,30,0,["eatk-1"],"Make squeaky cute sounds. Lower target's attack."],
            "Wine Vip": [35,"Grass",0,20,100,["crit1"],"Use Wine to hit target. Better chance to critical hit."],
            "Absorb": [20,"Grass",1,25,100,["hpd*"],"Use special power to absorb target's  hp. Can recover 50% HP of damage dealt."],
            "Injure": [40,"Poison",1,15,100,["psn%"],"Use poisonous leaf to attack. Might poison the target."],
            "Bite": [60,"Dark",0,20,100,["fln%"],"Use teeth to bite the target's body. Target might flinch."],
            "Mega Drain": [40,"Grass",1,20,100,["hpd*"],"Use special power to absorb a bunch of target's HP. Can recover 50% HP of damage dealt."],
            "Poison": [0,"Poison",1,15,95,["psn"],"Use poisonous liquid to poison the target."]
        }
        moves_levels = [
          3,
          5,
          6,
          8,
          10,
          11,
          13,
          16,
          17
        ]
        super().__init__("Mossprout", ["Grass"], moves, 55, 40, 65, 40, 65, 50, 5)

class Florisprout(Pokemon):
    def __init__(self):
        moves = {
            "Scratch": [30,"Normal",0,20,100,[None],"Use claws or hands to attack."],
            "Leafage": [40,"Grass",0,40,100,[None],"Use leaves to attack."],
            "Tackle": [40,"Normal",0,30,100,[None],"Use body to hit and attack."],
            "Growl": [0,"Normal",2,30,0,["eatk-1"],"Make squeaky cute sounds. Lower target's attack."],
            "Wine Vip": [35,"Grass",0,20,100,["crit1"],"Use Wine to hit target. Better chance to critical hit."],
            "Absorb": [20,"Grass",1,25,100,["hpd*"],"Use special power to absorb target's  hp. Can recover 50% HP of damage dealt."],
            "Injure": [40,"Poison",1,15,100,["psn%"],"Use poisonous leaf to attack. Might poison the target."],
            "Bite": [60,"Dark",0,20,100,["fln%"],"Use teeth to bite the target's body. Target might flinch."],
            "Mega Drain": [40,"Grass",1,20,100,["hpd*"],"Use special power to absorb a bunch of target's HP. Can recover 50% HP of damage dealt."],
            "Poison": [0,"Poison",1,15,95,["psn"],"Use poisonous liquid to poison the target."]
        }
        new_moves = {
            # Move Name: Damage, Type, Kind, PP, Accuracy, Special Effects
            # Kinds: 0 --> Physical ; 1 --> Special ; 2 --> Other
            # Accuracy 0 --> Can't Miss
            "Jumpscare": [0,"Normal",2,20,70,["eacc-1","espd-1],"Hide and suddenly show to scare target. Lower target's accuracy and speed."],
            "Magic Leaf": [60,"Grass",1,25,0,[None],"Use following leafs to attack. Can't miss."],
            "Seed Bomb": [80,"Grass",1,20,100,[None],"Use seed to attack."],
            "Poison Punch": [75,"Poison",0,20,100,["psn?"],"Fill the claws or hands with poisonous liquid then attack. Sometimes poisons the target."],
            "Toxic": [0,"Poison",2,15,0,["bps"],"Spread extremely poisonous liquid. Badl poisons the target."],
            "Work Up": [0,"Normal",2,20,0,["atk1","spa1"],"Make yourself feel better. Increases attack and special attack."],
            "Leaf Guard": [0,"Grass",2,20,0,["spd2"],"Use leaves to protect yourself. Sharply increase special defense."]
        }
        moves_levels = [
          18,
          21,
          24,
          28,
          30,
          33,
          35
        ]
        super().__init__("Florisprout", ["Grass"], moves, 75, 55, 80, 60, 80, 75, 18)

class Foliageon(Pokemon):
    def __init__(self):
        moves = {
            "Scratch": [30,"Normal",0,20,100,[None],"Use claws or hands to attack."],
            "Leafage": [40,"Grass",0,40,100,[None],"Use leaves to attack."],
            "Tackle": [40,"Normal",0,30,100,[None],"Use body to hit and attack."],
            "Growl": [0,"Normal",2,30,0,["eatk-1"],"Make squeaky cute sounds. Lower target's attack."],
            "Wine Vip": [35,"Grass",0,20,100,["crit1"],"Use Wine to hit target. Better chance to critical hit."],
            "Absorb": [20,"Grass",1,25,100,["hpd*"],"Use special power to absorb target's  hp. Can recover 50% HP of damage dealt."],
            "Injure": [40,"Poison",1,15,100,["psn%"],"Use poisonous leaf to attack. Might poison the target."],
            "Bite": [60,"Dark",0,20,100,["fln%"],"Use teeth to bite the target's body. Target might flinch."],
            "Mega Drain": [40,"Grass",1,20,100,["hpd*"],"Use special power to absorb a bunch of target's HP. Can recover 50% HP of damage dealt."],
            "Poison": [0,"Poison",1,15,95,["psn"],"Use poisonous liquid to poison the target."],
            "Jumpscare": [0,"Normal",2,20,70,["eacc-2"],"Hide and suddenly show to scare target. Harshly lower target's accuracy."],
            "Magic Leaf": [60,"Grass",1,25,0,[None],"Use following leafs to attack. Can't miss."],
            "Seed Bomb": [80,"Grass",1,20,100,[None],"Use seed to attack."],
            "Poison Punch": [75,"Poison",0,20,100,["psn?"],"Fill the claws or hands with poisonous liquid then attack. Sometimes poisons the target."],
            "Toxic": [0,"Poison",2,15,0,["bps"],"Spread extremely poisonous liquid. Badl poisons the target."],
            "Work Up": [0,"Normal",2,20,0,["atk1","spa1"],"Make yourself feel better. Increases attack and special attack."],
            "Leaf Guard": [0,"Grass",2,20,0,["spd2"],"Use leaves to protect yourself. Sharply increase special defense."]
        }
        new_moves = {
            # Move Name: Damage, Type, Kind, PP, Accuracy, Special Effects, Description
            # Kinds: 0 --> Physical ; 1 --> Special ; 2 --> Other
            # Accuracy 0 --> Can't Miss
            "Toxic Strike": [80,"Poison",1,20,0,["psn"],"Strike to the target with toxic. Can't miss and poisons the target. If uses on a target that is already poisoned, badly poisons it instead."],
            "Substitude": [0,"Normal",2,15,0,["hp--","stt"],"Sacrifice one quarter HP and create a substitude to protect itself."],
            "Giga Drain": [75,"Grass",1,10,100,["hpd*"],"Use special power to absorb a LOT of target's hp. Can recover 50% HP of damage dealt."],
            "Sleep Powder": [0,"Grass",2,15,75,["slp"],"Spread a bunch of powder that causes creatures to fall asleep. Can cause the target to fall sleep if hit."],
            "Stun Powder": [0,"Grass",2,30,75,["prz"],"Spread a bunch of powder that makes creatures hard to move. Paralyzes the target if hit."],
            "Wood Hammer": [120,"Grass",0,10,100,["hpd--"],"Use the extremely hard body to tackle the target. Takes big recoil."],
            "Water Punch": [85,"Water",0,20,100,[None],"Use water-powered hand to hurt the target."]
        }
        moves_levels = [
          36,
          42,
          48,
          55,
          56,
          62,
          70
        ]
        super().__init__("Foliageon", ["Grass","Poison"], moves, 90, 85, 90, 85, 90, 90, 36)

class Infernite:
  def __init__(self):
        moves = {
            "Tackle": [40,"Normal",0,20,100,[None],"Use body to hit and attack."],
        }
        new_moves = {
            # Move Name: Damage, Type, Kind, PP, Accuracy, Special Effects
            # Kinds: 0 --> Physical ; 1 --> Special ; 2 --> Other
            # Accuracy 0 --> Can't Miss
            "Ember": [40,"Fire",0,40,100,[None],"Use small flame to attack."],
            "Peck": [35,"Flying",0,35,100,[None],"Use sharp mouth to hit and attack."],
            "Leer": [0,"Normal",2,30,0,["edef-1"],"Make evil eye contact with target. Lower target's defense."],
            "Mental Damage": [30,"Psychic",0,20,100,["fln!"],"Use superpower to make target depressed. Big chance to make the target flinch. Cannot be used continiously."],
            "Twineedle": [25,"Bug",1,25,100,["a2","psn?"],"Tie two sting into target. Attack twice a row. Sometimes poisons the target."],
            "Power-Up Punch": [40,"Fighting",0,20,100,["atk1"],"Punch the target hardly. Raises users's attack."],
            "Flame Wheel": [60,"Fire",0,20,100,["brn?"],"Twist and rotate the body with fire-power. Sometimes burns the target."],
            "Will-O Wisp": [0,"Fire",2,30,85,["brn"],"Use dangerous fire to burn the target."],
            "Mean Look": [0,"Normal",2,20,0,["nes"],"Look at the target continiously. Prevent the target from escaping."]
        }
        moves_levels = [
          3,
          5,
          7,
          9,
          10,
          12,
          14,
          16,
          17
        ]
        super().__init__("Infernite", "Fire", moves, 55, 40, 65, 40, 65, 50, 5)
def newPoke(name, type,crm, moves, h, a, d, sa, sd, sp, nl, nm, lv):
  
  Pokemon().__init__(name, type, crm, moves, h, a, d, sa, sd, sp, nl, nm, lv)
