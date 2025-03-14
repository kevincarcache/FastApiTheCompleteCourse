from Enemy import *
import random

class Zombie(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__('Zombie', health_points, attack_damage)

    def talk(self):
        print(f'*Grumbling...*')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.50
        if did_special_attack_work:
            self.health_points += 2
            print(f'{self.get_type_of_enemy()} regenerated 2HP!')