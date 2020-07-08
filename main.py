from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

#Static power bar, etc for reference 
# print("\n \n")
# print("NAME                 HP                                       MP")
# print("                     _________________________                _________________________")
# print("Valos       220/460 |" + bcolors.okgreen + "█████████████████████████" + bcolors.ENDC + "|        65/65 |" + bcolors.okblue + "█████████████████████████" + bcolors.ENDC + "|")
# print("\n")

#create black magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 30, 700, "black")
blizzard = Spell("Blizzard", 20, 400, "black")
meteor = Spell("Meteor", 40, 1100, "black")
quake = Spell("Quake", 25, 850, "black")

#create white magic
cure = Spell("Cure", 25, 600, "white")
cura = Spell("Cura", 35, 1200, "white") 
player_spellsvid = [fire, thunder, blizzard, cure]
player_spellsjojo = [fire, thunder, blizzard, meteor, cure, cura]
player_spellsstevens = [blizzard, cure, cura]
enemy_spells = [fire, meteor, quake, cure]
#---------------------------------------------------------------------- 

#create some items 
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 10000)
hielixer = Item("Hi-Elixer", "elixer", "Fully restores HP/MP of party", 10000)
grenade = Item("Grenade", "attack", "Deals 500 Damage", 500)
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity": 5}, {"item": superpotion, "quantity": 3}, {"item": elixer, "quantity": 2}, 
              {"item": hielixer, "quantity": 1}, {"item": grenade, "quantity": 5}]

#instantiate the spells
player1 = Person("Jiten", 3000, 120, 400, 40, player_spellsvid, player_items) #attack guy
player2 = Person("Jagvi", 2000, 200, 150, 40, player_spellsjojo, player_items) #magic guy
player3 = Person("Suhru", 5000, 70, 250, 40, player_spellsstevens, player_items) #attack tank


#instantiate the enimies
enemy1 = Person("Imp        ", 3500, 500, 400, 23, enemy_spells, [])
enemy2 = Person("OG Two Tone", 11000, 400, 600, 23, enemy_spells, [])
enemy3 = Person("Simp       ", 2000, 500, 445, 23, enemy_spells, [])

#making all these bad boys players into lists for later 
players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)
while running:
       print("=================================================")
       print("\n")
       print("NAME                 HP                                       MP")
       
       for player in players:
              player.get_stats()
       
       print("\n")

       for enemy in enemies:
              enemy.enemy_get_stats()

       for player in players:
              player.choose_action()
              choice = input("\n" + "Choose Action: ")
              index = int(choice)-1
              alldead = False
              if index == 0:
                     dmg = player.generate_dmg()

                     enemy = player.choose_target(enemies)
                     enemies[enemy].take_dmg(dmg)

                     print("You attacked", enemies[enemy].name, "for,", dmg, "points of damage.")

                     if enemies[enemy].get_hp() == 0:
                            print(enemies[enemy].name, "has died!")
                            del enemies[enemy]
                            if len(enemies) == 0:
                                   alldead = True
                                   break

              elif index ==1:
                     player.choose_magic()
                     
                     magic_choice = int(input("\n" + "Choose Magic")) - 1  
                     if magic_choice == -1:
                            continue
                     spell = player.magic[magic_choice] #this just looks into the list of magic, which we have named player_spells, and then using the self.magic, this gets player.fire or whatever (which is a class i guess)
                     #so then spell is acc equal to like fire, thunder or whatever, and then the next line just does fire.generate_dmg() and gives a value 
                     magic_dmg = spell.generate_dmg() 

                     current_mp = player.get_mp()
                     


                     if spell.cost > current_mp:
                            print(bcolors.FAIL + "\n Not Enough MP \n" + bcolors.ENDC)
                            continue 


                     if spell.type == "white":
                            player.heal(magic_dmg)
                            print(bcolors.okblue + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
                     elif spell.type == "black":

                            enemy = player.choose_target(enemies)
                            enemies[enemy].take_dmg(magic_dmg)

                            player.reduce_mp(spell.cost)

                            print(bcolors.okblue + "\n" + spell.name + " deals", str(magic_dmg), " points of damage to", enemies[enemy].name, bcolors.ENDC)

                            
                            if enemies[enemy].get_hp() == 0:
                                   print(enemies[enemy].name, "has died!")
                                   del enemies[enemy]
                                   if len(enemies) == 0:
                                          alldead = True
                                          break

              elif index == 2:
                     player.choose_item()
                     item_choice = (int(input("Choose Item"))) - 1
                     
                     if item_choice == -1:
                            continue

                     item = player.items[item_choice]["item"]
                     
                     
                     if player.items[item_choice]["quantity"] == 0:
                            print(bcolors.FAIL + "\n" + "None left boyo..." + bcolors.ENDC)
                            continue

                     player.items[item_choice]["quantity"] -= 1

                     if item.type == "potion":
                            player.heal(item.prop)
                            print(bcolors.okgreen + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)
                     elif item.type =="elixer":

                            if item.name == "Hi-Elixer":
                                   for i in players:
                                          i.hp = i.maxhp
                                          i.mp = i.maxmp

                            else:
                                   player.hp = player.maxhp
                                   player.mp = player.maxmp

                            print(bcolors.okgreen + "\n" + item.name + "fully restores HP and MP." + bcolors.ENDC)
                     elif item.type =="attack":
                            enemy = player.choose_target(enemies)
                            enemies[enemy].take_dmg(item.prop)
                            print(bcolors.okgreen + "\n" + item.name + " deals", item.prop, "of damage to", enemies[enemy].name, bcolors.ENDC)

                            
                            if enemies[enemy].get_hp() == 0:
                                   print(enemies[enemy].name, "has died!")
                                   del enemies[enemy]
                                   if len(enemies) == 0:
                                          alldead = True
                                          break


       #check if the battle is already over, before attacking
       defeated_enemies = 0
       defeated_players = 0

       for enemy in enemies:
              if enemy.get_hp() == 0:
                     defeated_enemies += 1

       for player in players:
              if player.get_hp() == 0:
                     defeated_players += 1        

       if defeated_enemies == 2 or alldead == True:
              print(bcolors.okgreen + "It aint much but atleast you won at somethin" + bcolors.ENDC)
              running = False
       elif defeated_players == 2 or alldead == True:
              print((bcolors.FAIL + "How shitty is your life rn? LMFAOOOO" + bcolors.ENDC))
              running = False

       


       for enemy in enemies:
              enemy_choice = random.randrange(0, 2)
              if enemy_choice == 0:
                     target = random.randrange(0, len(players))
                     enemy_dmg = enemy.generate_dmg()

                     players[target].take_dmg(enemy_dmg)
                     print( enemy.name, "attacks " + players[target].name + " for", enemy_dmg)

              if enemy_choice == 1:
                     spell, magic_dmg = enemy.choose_enemy_spell()
                     enemy.reduce_mp(spell.cost)

                     if spell.type == "white":
                            enemy.heal(magic_dmg)
                            print(bcolors.okblue + "\n" + spell.name + " heals" + enemy.name +"for", str(magic_dmg), "HP." + bcolors.ENDC)
                     elif spell.type == "black":
                            target = random.randrange(0, len(players))
                            
                            players[target].take_dmg(magic_dmg)

                            print(bcolors.okblue + "\n" + enemy.name + " 's " + spell.name + " deals", str(magic_dmg), " points of damage to", players[target].name, bcolors.ENDC)

                            if players[target].get_hp() == 0:
                                   print("RIP", players[target].name)    
                                   del players[target]

                     # print("Enemy chose: ", spell, "damage is", magic_dmg)