import game_sub as sub
import random
from game_boss import Boss

stage = \
[
    range(10, 500, 40),
    range(10, 800, 30),
    range(10, 1500, 25)
]
end = [650, 950, 100000]

class Manager():
    def __init__(self) :
        self.time = 0
        self.stage_datas = stage
        self.ends = end
        
    def process(self, Main, stage):
        if stage == 0:
            for i in self.stage_datas[stage]:
                if self.time == i:
                    sub.enemy_gen_ground(Main)
        elif stage == 1:
            if self.time < 200:
                for i in self.stage_datas[stage]:
                    if self.time == i:
                        sub.enemy_gen_ground(Main)
            else:
                for i in self.stage_datas[stage]:
                    if self.time == i:
                        sub.enemy_gen_all(Main)
        else: # = stage 3 (BOSS)
            if self.time == 500:
                self.gen_BOSS(Main)
            for i in self.stage_datas[stage]:
                if self.time == i:
                    sub.enemy_gen_all(Main)
                
                
        self.time += 1
        if self.time == self.ends[stage]:
            Main.state = -1
            Main.stage += 1
            Main.money += 100
            Main.group_reset()
            self.time_reset()
                
    def time_reset(self):
        self.time = 0
        
    def gen_BOSS(self, Main):
        BOSS = Boss((1230, random.randint(400, 500)))
        Main.enemy_group.add(BOSS)
    