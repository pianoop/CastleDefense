import os
import pygame
import game_sub as sub
from game_enemy_effect import Enemy_effect
import math
current_path = os.path.dirname(__file__) 

enemy_projectile_imgs = \
[
    pygame.image.load(os.path.join(current_path, "enemy/Arrow01.png")),
    pygame.image.load(os.path.join(current_path, "enemy/Fire01.png")),
    pygame.image.load(os.path.join(current_path, "enemy/Ice01.png"))
]
enemy_projectile_dmg    = [20, 25, 40, 30, 50]
enemy_projectile_dpos   = [(-25, 0), (-15, 0), (-15, 15), (0, 0), (0, 0)]
gravity                 = 1

class Enemy_projectile(pygame.sprite.Sprite):
    def __init__(self, idx, pos):
        pygame.sprite.Sprite.__init__(self)
        self.idx = idx    
        self.dmg   = enemy_projectile_dmg[idx]    
        self.pos = pos
        self.dpos = enemy_projectile_dpos[idx]
        self.image = enemy_projectile_imgs[idx]
        self.rect = self.image.get_rect(center=self.pos)


    def update(self, Main):
        self.move(Main)

    def move(self, Main):
        if self.pos[0] <= 60:
            eft = Enemy_effect(self.idx, self.pos)
            Main.effect_group.add(eft)
                
            Main.castle.attacked(self.dmg, Main)
            self.kill()
        else:
            self.pos = sub.tup_sum(self.pos, self.dpos) 
            self.rect= self.image.get_rect(center = self.pos)
            
    