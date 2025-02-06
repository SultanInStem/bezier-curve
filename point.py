import pygame
from globals import to_screen_coords
class Point: 
    def __init__(self, pos, radius, color): 
        self.pos = pos 
        self.radius = radius 
        self.color = color


    def draw(self, screen): 
        screen_pos = to_screen_coords(self.pos)
        pygame.draw.circle(screen, self.color, (screen_pos[0], screen_pos[1]),self.radius, 0)

    def get_pos(self): 
        return self.pos

    def move(self, dr):
        self.pos = self.pos + dr 

    def set_pos(self, pos): 
        self.pos = pos 

    