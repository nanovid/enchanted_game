import random 
from classes.magic import Spell
from classes.inventory import Item

class bcolors:
       Header = '\033[95m'
       okblue = '\033[94m'
       okgreen = '\033[92m'
       WARNING = '\033[93m'
       FAIL = '\033[91m'
       ENDC = '\033[0m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'

class Person:
       def __init__(self, name, hp, mp, atk, df, magic, items):
              self.maxhp = hp
              self.hp = hp
              self.maxmp = mp
              self.mp = mp
              self.atkl = atk -10
              self.atkh = atk + 10 
              self.df = df
              self.magic = magic
              self.items = items
              self.actions = ["Attack", "Magic", "Items"]
              self.name = name

       def generate_dmg(self):
              return random.randrange(self.atkl, self.atkh)

       def take_dmg(self, dmg):
              self.hp = self.hp - dmg
              if self.hp < 0:
                     self.hp = 0
              return(self.hp)

       def heal(self, dmg):
              self.hp += dmg
              if self.hp > self.maxhp:
                     self.hp = self.maxhp

       def get_hp(self):
              return(self.hp)
       
       def get_maxhp(self):
              return(self.maxhp)
       
       def get_mp(self):
              return(self.mp)
       
       def get_maxmp(self):
              return(self.maxmp)

       def reduce_mp(self, cost):
              self.mp -= cost

       def choose_target(self, enemies):
              i = 1
              print("\n" + bcolors.FAIL + bcolors.BOLD + "    Target:" + bcolors.ENDC)
              for enemy in enemies:
                     print("      ", i, ". " + enemy.name)
                     i += 1
              choice = int(input("    Choose:")) -1
              return(choice)

       def choose_action(self):
              i = 1
              print("\n" + bcolors.BOLD + self.name + ":" +"\n"+ bcolors.ENDC)
              print("    Action")
              for item in self.actions:
                     print("    " + str(i) + ":" + item)
                     i += 1
       
       def choose_magic(self):
              i = 1
              
              print("\n" + bcolors.okblue + bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
              for spell in self.magic:
                     print("        " + str(i) + ":" + spell.name +  " (cost: " + str(spell.cost) + ")")
                     i += 1

       def choose_item(self):
              i = 1
              print("\n" + bcolors.okgreen + bcolors.BOLD + "    ITEM" + bcolors.ENDC)
              for item in self.items:
                     print("        " + str(i), ".", item["item"].name, ":", item["item"].description, "(x" + str(item["quantity"]) + ")")
                     i += 1

       def get_stats(self):
              
              hpbar = ""
              health_ticks = ((self.hp/self.maxhp)*25)
              magic_ticks = ((self.mp/self.maxmp)*10)
              mpbar = ""

              while health_ticks > 0:
                     hpbar += "█"
                     health_ticks -= 1

              while len(hpbar) < 25:
                     hpbar += " "

              while magic_ticks > 0:
                     mpbar += "█"
                     magic_ticks -= 1

              while len(mpbar) < 10:
                     mpbar += " "

              hp_string = str(self.hp) + "/" + str(self.maxhp)
              current_hp = ""

              if len(hp_string) < 9:
                     decreased = 9 - len(hp_string)
              
                     while decreased > 0:
                            current_hp += " "
                            decreased -= 1
                     current_hp += hp_string
              else:
                     current_hp = hp_string

       
              mp_string = str(self.mp) + "/" + str(self.maxmp)
              current_mp = ""

              if len(mp_string) < 7:
                     decreased2 = 7 - len(mp_string)
              
                     while decreased2 > 0:
                            current_mp += " "
                            decreased2 -= 1
                     current_mp += mp_string
              else:
                     current_mp = mp_string

              print("                       _________________________                  __________")
              print(self.name+"       "+ current_hp + " |" + bcolors.okgreen + hpbar + bcolors.ENDC + "|" + "        " + current_mp + " |" + bcolors.okblue + mpbar + bcolors.ENDC + "|")

       def enemy_get_stats(self):
              
              hpbar = ""
              health_ticks = round((self.hp/self.maxhp)*50)

              hp_string = str(self.hp) + "/" + str(self.maxhp)
              current_hp = ""

              while health_ticks > 0:
                     hpbar += "█"
                     health_ticks -= 1

              while len(hpbar) < 50:
                     hpbar += " "

              if len(hp_string) < 11:
                     decreased = 11 - len(hp_string)
              
                     while decreased > 0:
                            current_hp += " "
                            decreased -= 1
                     current_hp += hp_string
              else:
                     current_hp = hp_string

              print("                               __________________________________________________")
              print(self.name+"       "+ current_hp + " |" + bcolors.FAIL + hpbar + bcolors.ENDC + "|")

       def choose_enemy_spell(self):
              magic_choice = random.randrange(0, len(self.magic))
              spell = self.magic[magic_choice]
              magic_dmg = spell.generate_dmg()

              pct = (self.get_hp()/self.maxhp)*100

              if self.mp < spell.cost or spell.type == "white" and pct > 50:
                     return self.choose_enemy_spell()
              else:
                     return spell, magic_dmg