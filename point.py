import pygame
from globals import to_screen_coords
import math
import random
class Point: 
    def __init__(self, pos, radius, color): 
        self.pos = pos 
        self.radius = radius 
        self.color = color
        self.speed = 2
        self.angle = random.uniform(0, 2 * math.pi)
        self.target_angle = self.angle


    def draw(self, screen): 
        screen_pos = to_screen_coords(self.pos)
        pygame.draw.circle(screen, self.color, (screen_pos[0], screen_pos[1]),self.radius, 0)

    def get_pos(self): 
        return self.pos

    def move(self, dr):
        self.pos = self.pos + dr 

    def set_pos(self, pos): 
        self.pos = pos 

    def update(self): 
        if random.random() < 0.04: 
            self.target_angle = random.uniform(0,2*math.pi)

        x = self.pos[0]
        y = self.pos[1]
