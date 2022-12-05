import os
import pygame
import math

import game_sub as sub
from game_effect import Effect
from game_projectile import Projectile
from game_cooltime import Cooltime
current_path = os.path.dirname(__file__)


weapon_imgs = \
    [
    pygame.image.load(os.path.join(current_path, "weapon/Bow.png")),
    pygame.image.load(os.path.join(current_path, "weapon/Cannon.png")),
    pygame.image.load(os.path.join(current_path, "weapon/Bow2.png")),
    pygame.image.load(os.path.join(current_path, "weapon/Cane.png"))
    ]
weapon_poses = [(60, 380), (30, 380), (60, 380), (60, 380)]
weapon_speeds= [25, 25, 30, 100]

skill_imgs = \
[
pygame.image.load(os.path.join(current_path, "skill/Bow1.png")),
pygame.image.load(os.path.join(current_path, "skill/Cannon.png")),
pygame.image.load(os.path.join(current_path, "skill/Bow2.png")),
pygame.image.load(os.path.join(current_path, "skill/Fire.png"))
]
skill_pos = [(880, 620), (980, 620), (1080, 620), (1180, 620)]

class Weapons():
    def __init__(self):
        super().__init__()
        self.imgs = weapon_imgs
        self.skill_imgs = skill_imgs
        self.skill_pos = skill_pos
        
        self.poses = weapon_poses
        self.speed = weapon_speeds
        self.rct = []
        for idx, img in enumerate(self.imgs):
            self.rct.append(img.get_rect(center = self.poses[idx]))
        
        self.now    = 0  # 시작 기본 무기 bow
        self.image  = self.imgs[self.now]
        self.rect   = self.imgs[self.now].get_rect(center = self.poses[self.now])
        
        self.lock   = [1, 0, 0 ,0]
        self.cool_lock = [1, 1, 1, 1]
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        for idx, on in enumerate(self.lock):
            if on:
                screen.blit(self.skill_imgs[idx], self.skill_pos[idx])
                
        
    def update(self):
        self.rotate()
        
    def rotate(self):
        angle = sub.calc_angle(self.rct[self.now])
        self.image = pygame.transform.rotate(self.imgs[self.now], -int(math.degrees(angle)))
        self.rect = self.image.get_rect(center=self.poses[self.now])
    
    def keydown(self, key):
        if key == pygame.K_1:
            self.swap(0)
        elif key == pygame.K_2:
            if self.lock[1]:
                self.swap(1)
        elif key == pygame.K_3:
            if self.lock[2]:
                self.swap(2)
        elif key == pygame.K_4:
            if self.lock[3]:
                self.swap(3)
    
    def swap(self, weapon):
        self.now = weapon
        self.image = self.imgs[self.now]
        self.rect  = self.rct[self.now]

    def attack(self, Main):
            if self.now == 0:
                if self.cool_lock[self.now]:
                    self.cool_lock[self.now] = 0
                    cool_eft = Cooltime(self.now)
                    Main.cool_group.add(cool_eft)
                    self.attack_bow(Main)
            elif self.now == 1:
                if self.cool_lock[self.now]:
                    self.cool_lock[self.now] = 0
                    cool_eft = Cooltime(self.now)
                    Main.cool_group.add(cool_eft)
                    self.attack_cannon(Main)
            if self.now == 2:
                if self.cool_lock[self.now]:
                    self.cool_lock[self.now] = 0
                    cool_eft = Cooltime(self.now)
                    Main.cool_group.add(cool_eft)
                    self.attack_bow(Main)
            elif self.now == 3:
                if self.cool_lock[self.now]:
                    self.cool_lock[self.now] = 0
                    cool_eft = Cooltime(self.now)
                    Main.cool_group.add(cool_eft)
                    self.attack_wand(Main)

    def attack_bow(self, Main):
        angle = sub.calc_angle(self.rct[self.now])
        dpos = (math.sin(angle) * self.speed[self.now], -math.cos(angle) * self.speed[self.now])
        projectile = Projectile(self.now, dpos, angle)
        Main.projectile_group.add(projectile)

    def attack_cannon(self, Main):
        angle = sub.calc_angle(self.rct[self.now])
        dpos = (math.sin(angle) * self.speed[self.now], -math.cos(angle) * self.speed[self.now])
        projectile = Projectile(self.now, dpos, angle)
        Main.projectile_group.add(projectile)

    def attack_wand(self, Main):
        eft = Effect(self.now, pygame.mouse.get_pos())
        Main.effect_group.add(eft)
        
    def reset(self):
        self.lock   = [1, 0, 0 ,0]
        
    def cool_reset(self):
        self.cool_lock = [1, 1, 1, 1]