from Enemy import *
import random

class Ogre(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__('Ogre', health_points, attack_damage)

    def talk(self):
        print(f'{self.get_type_of_enemy()} is slamming hands all around!')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.20
        if did_special_attack_work:
            self.attack_damage += 4
            print(f'{self.get_type_of_enemy()} get angry and increases attack by 4!')