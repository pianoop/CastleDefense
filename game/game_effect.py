import pygame
import os
import random
import game_sub as sub
current_path = os.path.dirname(__file__) 


effect_imgs = \
[
    [
    pygame.image.load(os.path.join(current_path, "sprite/arrow01.png")),
    pygame.image.load(os.path.join(current_path, "sprite/arrow02.png")),
    pygame.image.load(os.path.join(current_path, "sprite/arrow03.png")),
    pygame.image.load(os.path.join(current_path, "sprite/arrow04.png")),
    pygame.image.load(os.path.join(current_path, "sprite/arrow05.png"))
    ],
    [
    pygame.image.load(os.path.join(current_path, "sprite/Cannonball01.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Cannonball02.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Cannonball03.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Cannonball04.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Cannonball05.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Cannonball06.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Cannonball07.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Cannonball08.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Cannonball09.png"))
    ],
    [
    pygame.image.load(os.path.join(current_path, "sprite/Magic01.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Magic02.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Magic03.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Magic04.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Magic05.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Magic06.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Magic07.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Magic08.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Magic09.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Magic10.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Magic11.png"))
    ],
    [
    pygame.image.load(os.path.join(current_path, "sprite/Fire00.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire01.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire02.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire03.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire04.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire05.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire06.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire07.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire08.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire09.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire10.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire11.png")),
    pygame.image.load(os.path.join(current_path, "sprite/Fire12.png"))
    ]
]

effect_dmg = [0, 10, 15, 20]

class Effect(pygame.sprite.Sprite):
    def __init__(self, idx, pos):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = effect_imgs[idx]
        self.dmg  = effect_dmg[idx]
        self.pos = pos
        self.zero = idx
        self.idx = idx
        self.e_idx = 1
        self.interval = 3
        self.end = self.interval * len(self.imgs)
        self.image = self.imgs[self.e_idx]
        self.rect  = self.imgs[self.e_idx // self.interval].get_rect(center = pos)
        

    def update(self, Main):
        if self.e_idx >= self.end:
            self.kill()
        else:
            self.image = self.imgs[self.e_idx // self.interval]
            self.rect= self.image.get_rect(center = self.pos)
            self.e_idx += 1
        if self.zero != 0:
            self.check_colider(Main)

    def check_colider(self, Main):
        enemy = pygame.sprite.spritecollide(self, Main.enemy_group, False, pygame.sprite.collide_mask)
        if enemy:
            for enm in enemy:
                eft = Effect(0, sub.tup_sum(enm.pos, (random.randint(-30,30), random.randint(-30,30))))
                Main.effect_group.add(eft)
                enm.attacked(self.dmg, Main)