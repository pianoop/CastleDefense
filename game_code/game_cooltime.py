import os
import pygame

current_path = os.path.dirname(__file__)

cooldown_imgs = \
[
pygame.image.load(os.path.join(current_path, "skill/cooldown01.png")),
pygame.image.load(os.path.join(current_path, "skill/cooldown02.png")),
pygame.image.load(os.path.join(current_path, "skill/cooldown03.png")),
pygame.image.load(os.path.join(current_path, "skill/cooldown04.png")),
pygame.image.load(os.path.join(current_path, "skill/cooldown05.png"))
]

skill_pos = [(880, 620), (980, 620), (1080, 620), (1180, 620)]
skill_interval = [1, 6, 16, 24]
skill_cool = [5, 30, 80, 120]

class Cooltime(pygame.sprite.Sprite):
    def __init__(self, idx):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.imgs = cooldown_imgs
        for img in self.imgs:
            img.set_alpha(96)
        self.idx = idx
        self.image = self.imgs[0]
        self.pos = skill_pos[idx]
        self.rect  = self.image.get_rect(topleft=self.pos)
        
        self.w_idx = 0
        self.w_interval = skill_interval[idx]
        self.end = skill_cool[idx]
        
    def update(self, Main):
        if self.w_idx >= self.end:
            Main.weapon.cool_lock[self.idx] = 1
            self.kill()
        else:
            self.image = self.imgs[self.w_idx // self.w_interval]
            self.w_idx += 1