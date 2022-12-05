import os
import pygame

castle_hp           =   314
current_path = os.path.dirname(__file__)

game_start = pygame.image.load(os.path.join(current_path, "bg/gamestart.png"))
game_start_pos = (450, 460)

game_text = pygame.image.load(os.path.join(current_path, "bg/text.png"))
game_text_pos = (750, 460)

game_page = pygame.image.load(os.path.join(current_path, "bg/page.png"))
game_page_pos = (600, 400)

game_X = pygame.image.load(os.path.join(current_path, "bg/X.png"))
game_X_pos = (830, 280)

game_home = pygame.image.load(os.path.join(current_path, "bg/Home.png"))
game_home_pos = (780, 290)

gameover_restart = pygame.image.load(os.path.join(current_path, "bg/Restart.png"))
gameover_restart_pos = (550, 420)

gameover_home = game_home
gameover_home_pos = (800, 420)



class System():
    def __init__(self):
        super().__init__()
        self.game_start_pos = game_start_pos
        self.game_start = game_start
        self.game_start_rct = game_start.get_rect(center= game_start_pos)
        
        self.game_text_pos = game_text_pos
        self.game_text = game_text
        self.game_text_rct = game_text.get_rect(center= game_text_pos)
        
        self.game_page_pos = game_page_pos
        self.game_page = game_page
        self.game_page_rct = game_page.get_rect(center= game_page_pos)
        
        self.game_X_pos = game_X_pos
        self.game_X = game_X
        self.game_X_rct = game_X.get_rect(center= game_X_pos)
        
        self.game_home_pos = game_home_pos
        self.game_home = game_home
        self.game_home_rct = game_home.get_rect(center= game_home_pos)
        
        self.gameover_restart_pos = gameover_restart_pos
        self.gameover_restart = gameover_restart
        self.gameover_restart_rct = gameover_restart.get_rect(center= gameover_restart_pos)
        
        self.gameover_home_pos = gameover_home_pos
        self.gameover_home = gameover_home
        self.gameover_home_rct = gameover_home.get_rect(center= gameover_home_pos)
        
        self.text_on = 0
        
    def update(self, Main):
        pass
    
    def draw_title(self,screen, Main):
        if self.text_on:
            screen.blit(self.game_page, self.game_page_rct)
            screen.blit(self.game_X, self.game_X_rct)
        else:
            screen.blit(self.game_start, self.game_start_rct)
            screen.blit(self.game_text, self.game_text_rct)
        
    def collide_title(self, Main, mouse_pos):
        if self.text_on:
            if self.game_X_rct.collidepoint(mouse_pos):
                self.text_on = 0
        else:
            if self.game_start_rct.collidepoint(mouse_pos):
                Main.state = 1
                Main.group_reset()
            if self.game_text_rct.collidepoint(mouse_pos):
                self.text_on = 1
    
    def draw_gameover(self,screen, Main):
        screen.blit(self.gameover_restart, self.gameover_restart_rct)
        screen.blit(self.gameover_home, self.gameover_home_rct)
    
    def collide_gameover(self, Main, mouse_pos):
        if self.gameover_restart_rct.collidepoint(mouse_pos):
            Main.state = 1
            Main.money = Main.save_money
            Main.castle.hpbar.set_hp(Main.save_hp)
            Main.group_reset()
            
        if self.gameover_home_rct.collidepoint(mouse_pos):
            self.reset(Main)
    
    def draw_gameclear(self,screen, Main):
        screen.blit(self.game_home, self.game_home_rct)
    
    def collide_gameclear(self, Main, mouse_pos):
        if self.game_home_rct.collidepoint(mouse_pos):
            self.reset(Main)
            
    def reset(self, Main):
        Main.money = 0
        Main.save_money = 0
        Main.castle.hpbar.set_hp(castle_hp)
        self.save_hp = castle_hp
        Main.weapon.reset()
        Main.weapon.cool_reset()
        Main.stage = 0
        Main.state = 0
        Main.group_reset()
        
        