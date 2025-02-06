import pygame
import sys
from globals import SCREEN_SIZE
from point import Point
import numpy as np 
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Bezier Curve")
        self.running = True
        self.fps = 90
        self.end_points = [
            Point(np.array([-100,0]),  10, (255,255,255)), 
            Point(np.array([100,100]), 10, (255,255,255))
        ]
        self.control_points = [
            Point(np.array([0,100]), 5, (0,100,100)), 
            Point(np.array([50,100]), 5, (0,100,100)) 
        ]




    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 

    def update(self):
        pass

    def render(self): 
        self.screen.fill((0,0,0))


        for p in self.control_points: 
            p.draw(self.screen)

        for p in self.end_points: 
            p.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()