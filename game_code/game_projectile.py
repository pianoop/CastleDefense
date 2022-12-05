import os
import pygame
import game_sub as sub
from game_effect import Effect
import math
current_path = os.path.dirname(__file__) 

projectile_imgs = [
    pygame.image.load(os.path.join(current_path, "weapon/Arrow.png")),
    pygame.image.load(os.path.join(current_path, "weapon/Cannonball.png")),
    pygame.image.load(os.path.join(current_path, "weapon/Arrow2.png"))]
projectile_poses = [(70, 380), (70, 360), (70, 380)]
projectile_dmg   = [50, 20, 10]
gravity          = 1


class Projectile(pygame.sprite.Sprite):
    def __init__(self, idx, dpos = (0, 0), angle = 0):
        pygame.sprite.Sprite.__init__(self)
        self.idx = idx    
        self.dmg   = projectile_dmg[idx]    
        if idx == 0 or idx == 2:
            self.image = pygame.transform.rotate(projectile_imgs[self.idx], -(int(math.degrees(angle))))
        else:
            self.image = projectile_imgs[idx]
        self.pos = projectile_poses[idx]
        self.dpos = dpos
        self.angle = angle
        
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, Main):
        self.move()
        if not(sub.range_check(self.pos)):
            self.kill()
        self.check_colider(Main)

    def move(self):
        if(self.idx == 0):
            self.move_arrow()
        elif(self.idx== 1):
            self.move_cannonball()
        elif(self.idx== 2):
            self.move_arrow()
        elif(self.idx== 3):
            self.move_magic()

    def move_arrow(self):
        self.pos = self.pos[0] + self.dpos[0], self.pos[1] + self.dpos[1] 
        self.rect.center = self.pos
        
    def move_cannonball(self):
        self.pos = self.pos[0] + self.dpos[0], self.pos[1] + self.dpos[1] 
        self.rect.center = self.pos
        self.dpos = self.dpos[0], self.dpos[1] + gravity
        
    def move_magic(self):
        pass
    
    def check_colider(self, Main):
        enemy = pygame.sprite.spritecollide(self, Main.enemy_group, False, pygame.sprite.collide_mask)
        if enemy:
            enemy[0].attacked(self.dmg, Main)
            eft = Effect(self.idx, self.pos)
            Main.effect_group.add(eft)
            self.kill()
    