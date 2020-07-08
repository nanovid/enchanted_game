import random


class Spell:
       def __init__(self, name, cost, damage, type_):
              self.name = name
              self.cost = cost
              self.damage = damage
              self.type = type_  

       def generate_dmg(self):
               low = self.damage - 15
               high = self.damage + 15  
               return(random.randrange(low, high))    

