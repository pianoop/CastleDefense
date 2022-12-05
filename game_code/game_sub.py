import os
import pygame
import math
import random
from game_enemy import Enemy

screen_width        =   1280
screen_height       =   720
angle90             =   math.pi * 3 / 4
transColor          =   pygame.Color(0, 0, 0)

def range_check(pos):
    return (pos[0] >=0) and (pos[0] <= screen_width) and (pos[1] >= 0) and (pos[1] <= screen_height)

def calc_angle(rct):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return math.pi - math.atan2(mouse_x - rct.centerx, mouse_y - rct.centery)
    
def enemy_gen_ground(Main):
    enemy = Enemy(random.randint(0, 2))
    Main.enemy_group.add(enemy)
    
def enemy_gen_all(Main):
    enemy = Enemy(random.randint(0, 4))
    Main.enemy_group.add(enemy)
    
def tup_sum(pos1, pos2):
    return (pos1[0] + pos2[0], pos1[1] + pos2[1])