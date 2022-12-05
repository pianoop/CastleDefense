import os
import pygame

castle_hp           =   314

current_path = os.path.dirname(__file__)

shop_skill_imgs = \
[
pygame.image.load(os.path.join(current_path, "skill/shop/Cannon_shop.png")),
pygame.image.load(os.path.join(current_path, "skill/shop/Bow2_shop.png")),
pygame.image.load(os.path.join(current_path, "skill/shop/Fire_shop.png"))
]

shop_etc_imgs = \
[
pygame.image.load(os.path.join(current_path, "skill/shop/castle_repair.png"))
]

shop_skill_pos   =  [(400, 250), (600, 250), (800, 250)]
shop_etc_pos     =  [(400, 550)]
shop_skill_price =  [150, 200, 250]
shop_etc_price   =  [100]

shop_off_imgs = \
[
pygame.image.load(os.path.join(current_path, "skill/shop/Cannon_off.png")),
pygame.image.load(os.path.join(current_path, "skill/shop/Bow2_off.png")),
pygame.image.load(os.path.join(current_path, "skill/shop/Fire_off.png"))
]

shop_skill_rcts = \
[
shop_skill_imgs[0].get_rect(center = shop_skill_pos[0]),
shop_skill_imgs[1].get_rect(center = shop_skill_pos[1]),
shop_skill_imgs[2].get_rect(center = shop_skill_pos[2])
]

shop_etc_rcts = \
[
shop_etc_imgs[0].get_rect(center = shop_etc_pos[0])
]

next_stage_img = pygame.image.load(os.path.join(current_path, "skill/shop/next_stage.png"))
next_pos = (1150, 650)

class Shop():
    def __init__(self):
        super().__init__()
        self.skill_imgs = shop_skill_imgs
        self.skill_poses = shop_skill_pos
        self.skill_rcts = shop_skill_rcts
        self.skill_price = shop_skill_price
         
        self.etc_imgs = shop_etc_imgs
        self.etc_poses = shop_etc_pos
        self.etc_price = shop_etc_price
        self.etc_rcts = shop_etc_rcts
            
        self.off_imgs = shop_off_imgs
        
        self.next_stage_img = next_stage_img
        self.next_pos = next_pos
        self.next_rct = self.next_stage_img.get_rect(center = self.next_pos)
        
    def update(self, Main):
        pass
    
    def draw(self, Main, screen):
        for idx, rct in enumerate(self.skill_rcts):
            if Main.weapon.lock[idx + 1] == 0:
                screen.blit(self.skill_imgs[idx], rct)
            else:
                screen.blit(self.off_imgs[idx], rct)
            
        for idx, rct in enumerate(self.etc_rcts):
            screen.blit(self.etc_imgs[idx], rct)
        
        screen.blit(self.next_stage_img, self.next_rct)
            
    def collide(self, Main, mouse_pos):
        for idx, rct in enumerate(self.skill_rcts):
            if rct.collidepoint(mouse_pos):
                if Main.money >= self.skill_price[idx] and Main.weapon.lock[idx + 1] == 0:
                    Main.weapon.lock[idx + 1] = 1
                    Main.money -= self.skill_price[idx]
                    return
        
        for idx, rct in enumerate(self.etc_rcts):
            if rct.collidepoint(mouse_pos):
                if Main.money >= self.etc_price[idx] and Main.castle.hpbar.get_hp() < castle_hp:
                    Main.money -= self.etc_price[idx]
                    Main.castle.hpbar.set_hp(castle_hp)
                    # 성이 수리되었습니다 문구
                    return
                
        if self.next_rct.collidepoint(mouse_pos):
            Main.save_money = Main.money
            Main.state = 1
        