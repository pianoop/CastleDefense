import pygame
import os

import game_sub as sub
from game_boss_projectile import Boss_projectile
from game_hp import Hpbar

current_path = os.path.dirname(__file__) 

boss_imgs = [pygame.image.load(os.path.join(current_path, "enemy/Boss/PyThonny.png"))
    ]
boss_speed  = 1
cooltime = (140, 280)
boss_hp =   5024

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        hpbar_pos = sub.tup_sum(pos, (-200, -150))
        self.hpbar = Hpbar(boss_hp >> 4, hpbar_pos, hpbar_pos)
        
        self.imgs = boss_imgs
        self.pos = pos
        self.image = self.imgs[0]
        self.rect = self.image. get_rect(center = pos)
        
        self.range = 700
        self.speed = boss_speed
        self.hp = boss_hp
        self.cnt = 0
        self.patternA, self.patternB = cooltime
        
    def update(self, Main, screen):
        self.move()
        self.attack(Main)
        self.hpbar.draw(screen)
        
    def move(self):
        if self.pos[0] > self.range:
            self.pos = self.pos[0] - self.speed, self.pos[1]
            self.rect = self.image.get_rect(center=self.pos)
        self.hpbar.update(self.pos)
            
    def attack(self, Main):
        self.cnt += 1
        
        if self.cnt == self.patternA:
            patternA = Boss_projectile(0, sub.tup_sum(self.pos, (-60, -90)))
            Main.enemy_projectile_group.add(patternA)
        elif self.cnt == self.patternB:
            patternB = Boss_projectile(1, sub.tup_sum(self.pos, (90, -30)))
            Main.enemy_projectile_group.add(patternB)
            self.cnt = 0
                           
    def attacked(self, dmg, Main):
        self.hp -= dmg
        self.hpbar.set_hp(self.hp >> 4)
        if self.hp <= 0:
            Main.money += 1000
            Main.state = -3
            Main.group_reset()
            self.kill()            