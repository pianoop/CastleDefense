import os
import pygame
import game_sub as sub
from game_enemy_effect import Enemy_effect
import math
current_path = os.path.dirname(__file__) 

boss_projectile_imgs = \
[
    [
        pygame.image.load(os.path.join(current_path, "enemy/Boss/ex_fire01.png")),
        pygame.image.load(os.path.join(current_path, "enemy/Boss/ex_fire02.png")),
        pygame.image.load(os.path.join(current_path, "enemy/Boss/ex_fire03.png"))
    ],
    [
        pygame.image.load(os.path.join(current_path, "enemy/Boss/tornado01.png")),
        pygame.image.load(os.path.join(current_path, "enemy/Boss/tornado02.png")),
        pygame.image.load(os.path.join(current_path, "enemy/Boss/tornado03.png"))
    ]
]
boss_projectile_dmg    = [200, 200]
boss_projectile_dpos   = [(-2, 0), (-3, 0)]
effect_idx             = [3, 4]
counter                = [3, 2]
fail                   = [0, 3, 0, 0]
gravity                 = 1

class Boss_projectile(pygame.sprite.Sprite):
    def __init__(self, idx, pos):
        pygame.sprite.Sprite.__init__(self)
        self.idx = idx    
        self.dmg   = boss_projectile_dmg[idx]    
        self.pos = pos
        self.dpos = boss_projectile_dpos[idx]
        self.imgs = boss_projectile_imgs[idx]
        self.effect_idx = effect_idx[idx]
        self.counter_idx    = counter[idx]
        
        self.w_idx = 1
        self.w_interval = 4
        self.w_end = self.w_interval * len(self.imgs)
        self.image = self.imgs[0]
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, Main):
        if Main.state != 1:
            self.kill()
        self.move(Main)
        self.check_colider(Main)

    def move(self, Main):
        if self.pos[0] <= 170:
            eft = Enemy_effect(self.effect_idx, sub.tup_sum(self.pos,(-150, 0)))
            Main.enemy_effect_group.add(eft)
            Main.castle.attacked(self.dmg)
            self.kill()
        else:
            self.pos = sub.tup_sum(self.pos, self.dpos) 
            self.image = self.imgs[self.w_idx // self.w_interval]
            self.rect= self.image.get_rect(center = self.pos)
            self.w_idx += 1
            if self.w_idx >= self.w_end:
                self.w_idx = 1
            
    def check_colider(self, Main):
        projectile = pygame.sprite.spritecollide(self, Main.projectile_group, False, pygame.sprite.collide_mask)
        if self.idx == 1:
            if projectile:
                for pjt in projectile:
                    if pjt.idx == self.counter_idx:
                        eft = Enemy_effect(self.effect_idx, self.pos)
                        Main.enemy_effect_group.add(eft)
                        self.kill()
                    else:
                        eft = Enemy_effect(fail[pjt.idx], pjt.pos)
                        Main.enemy_effect_group.add(eft)
                        pjt.kill()
            effect = pygame.sprite.spritecollide(self, Main.effect_group, False, pygame.sprite.collide_mask)
            if effect:
                for eft in effect:
                    if eft.idx == 2:
                        eft = Enemy_effect(self.effect_idx, self.pos)
                        Main.enemy_effect_group.add(eft)
                        self.kill()
                    eft.kill()
        else:
            if projectile:
                for pjt in projectile:
                    eft = Enemy_effect(fail[pjt.idx], pjt.pos)
                    Main.enemy_effect_group.add(eft)
                    pjt.kill()
            effect = pygame.sprite.spritecollide(self, Main.effect_group, False, pygame.sprite.collide_mask)
            if effect:
                for eft in effect:
                    if eft.idx == 3:
                        eft = Enemy_effect(self.effect_idx, self.pos)
                        Main.enemy_effect_group.add(eft)
                        self.kill()
                    else:
                        eft.kill()
