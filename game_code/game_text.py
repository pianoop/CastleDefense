import os
import pygame
current_path = os.path.dirname(__file__) 
pygame.font.init()
WHITE   = (255, 255, 255)
YELLOW  = (255, 255, 0)
R       = (255, 153, 153)
B       = (204, 204, 255)
BLACK   = (0, 0, 0)

font_bigbig = pygame.font.Font(current_path + '/font/Maplestory_Bold.ttf', 120)
font_big = pygame.font.Font(current_path + '/font/Maplestory_Bold.ttf', 60)
font_bb = pygame.font.Font(current_path + '/font/Maplestory_Bold.ttf', 45)
font_b = pygame.font.Font(current_path + '/font/Maplestory_Light.ttf', 40)
font = pygame.font.Font(current_path + '/font/Maplestory_Light.ttf', 30)
font_s = pygame.font.Font(current_path + '/font/Maplestory_Light.ttf', 20)

shop1 = [font_big.render('상점', True, WHITE)]
shop1_pos = [(100, 120)]

shop2 = \
[
font_big.render('스킬', True, R),
font_big.render('기타', True, B),
font.render('150 G', True, YELLOW),
font.render('200 G', True, YELLOW),
font.render('250 G', True, YELLOW)
]
shop2_pos = [(180, 220), (180, 520), (320, 350), (520, 350), (720, 350)]

shop3 = \
[
font.render('성 수리 100 G', True, YELLOW)
]
shop3_pos = [(320, 650)]

shop4 = \
[
font.render('다음 스테이지로', True, WHITE)
]
shop4_pos = [(900, 650)]


money_pos = (0, 70)
stage_pos = (0, 0)

title = \
[
font_bigbig.render('Castle', True, R),
font_bigbig.render('Defense', True, R),
font.render('무시무시한 마물로부터 성을 지켜내세요!', True, WHITE),
font_bb.render('게임 설명', True, WHITE)
]

title_pos = [(300, 50), (450, 150), (200, 600), (660, 430)]

title_text = \
[
font.render('1, 2, 3, 4로 무기를 변경합니다.', True, WHITE),
font.render('(상점에서 추가 구매)', True, WHITE),
font.render('마우스 클릭으로 공격할 수 있습니다.', True, WHITE),
font.render('(좌, 우, 휠 모두 가능)', True, WHITE)
]

title_text_pos = [(400, 300), (400, 350), (400, 400), (400, 450)]

gameover = \
[
font_bigbig.render('패배!', True, BLACK),
font_b.render('재도전', True, WHITE),
font_b.render('타이틀로', True, WHITE)
]

gameover_pos = [(480, 250), (400, 400), (620, 400)]

gameclear = \
[
font_big.render('승리!', True, YELLOW),
font_b.render('플레이해주셔서 감사합니다.', True, WHITE),
font_s.render('by pianop', True, WHITE),
font_b.render('타이틀로', True, BLACK)
]

gameclear_pos = [(600, 120), (400, 200), (800, 240), (600, 270)]

class Text():
    def __init__(self):
        super().__init__()
        self.shop1      = shop1
        self.shop1_pos  = shop1_pos
        self.shop2      = shop2
        self.shop2_pos  = shop2_pos
        self.shop3      = shop3
        self.shop3_pos  = shop3_pos
        self.shop4      = shop4
        self.shop4_pos  = shop4_pos
        
        self.money_pos = money_pos
        self.stage_pos = stage_pos
        
        self.title = title
        self.title_pos = title_pos
        
        self.title_text = title_text
        self.title_text_pos = title_text_pos
        
        self.gameover = gameover
        self.gameover_pos = gameover_pos
        
        self.gameclear = gameclear
        self.gameclear_pos = gameclear_pos
    
    def draw_shop(self, screen, Main):
        for idx, text in enumerate(self.shop1):
            screen.blit(text, self.shop1_pos[idx])
        for idx, text in enumerate(self.shop2):
            screen.blit(text, self.shop2_pos[idx])
        for idx, text in enumerate(self.shop3):
            screen.blit(text, self.shop3_pos[idx])
        for idx, text in enumerate(self.shop4):
            screen.blit(text, self.shop4_pos[idx])    
        screen.blit(font_big.render(str(Main.money)+' G', True, YELLOW), self.money_pos)

    
    def draw_stage(self, screen, Main):
        screen.blit(font_big.render('Stage: ' + str(Main.stage + 1), True, WHITE), self.stage_pos)
        screen.blit(font_big.render(str(Main.money)+' G', True, YELLOW), self.money_pos)
    
    def draw_title(self, screen, Main):
        if Main.system.text_on:
            for idx, text in enumerate(self.title_text):
                screen.blit(text, self.title_text_pos[idx])
        else:
            for idx, text in enumerate(self.title):
                screen.blit(text, self.title_pos[idx])
    
    def draw_gameover(self, screen):
        for idx, text in enumerate(self.gameover):
            screen.blit(text, self.gameover_pos[idx])
    
    def draw_gameclear(self, screen):
        for idx, text in enumerate(self.gameclear):
            screen.blit(text, self.gameclear_pos[idx])