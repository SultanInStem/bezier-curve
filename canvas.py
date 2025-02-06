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
        self.running = True
        self.fps = 90

        self.point_o    =   Point(np.array([-100,0]),  10, (255,255,255))
        self.point_test =   Point(np.array([-100,0]),  10, (255,0,0))
        self.point_f    =   Point(np.array([100,100]), 10, (255,255,255))



        self.t_max = np.linalg.norm(self.point_f.get_pos() - self.point_o.get_pos())
        self.t_min = 0 

        self.dir_vector = ((self.point_f.get_pos() - self.point_o.get_pos()) / self.t_max) * 1.1

        pygame.display.set_caption("Bezier Curve")


    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 

    def update(self):
        self.point_test.move(self.dir_vector) 

    def render(self): 
        self.screen.fill((0,0,0))

        self.point_o.draw(self.screen)
        self.point_f.draw(self.screen)
        self.point_test.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()