import pygame
import sys
from globals import SCREEN_SIZE, to_math_coords, to_screen_coords
from point import Point
import numpy as np 
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Bezier Curve")
        self.running = True
        self.dragging = False
        self.dragging_index = 0
        self.fps = 90
        self.t = 0
        self.dt = 0.01
        self.points = [
            Point(np.array([-100,0]),  20, (255,255,255)), 
            Point(np.array([0,100]), 5, (0,100,100)), 
            # Point(np.array([50,100]), 5, (0,100,100)), 
            Point(np.array([100,100]), 20, (255,255,255))
        ]

        self.trace = []

    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
            

            if event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = to_math_coords(np.array([event.pos[0], event.pos[1]]))
                for i in range(0, len(self.points)): 
                    point_pos = self.points[i].get_pos()
                    dist = np.linalg.norm(point_pos - mouse_pos)
                    if dist < self.points[i].radius: 
                        self.dragging = True
                        self.dragging_index = i

            if event.type == pygame.MOUSEMOTION and self.dragging: 
                mouse_pos = to_math_coords(np.array([event.pos[0], event.pos[1]]))
                self.points[self.dragging_index].set_pos(mouse_pos)

            if event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False  
                    

            

    def update(self):
        if self.t >= 1: return
        self.t += self.dt 
        pos = (self.points[2].get_pos() - self.points[1].get_pos()) - (self.points[1].get_pos() - self.points[0].get_pos())
        pos = pos * (self.t) * (self.t)
        pos = to_screen_coords(pos)
        self.trace.append((pos[0], pos[1]))

    def render(self): 
        self.screen.fill((0,0,0))


        for p in self.points: 
            p.draw(self.screen)

        for p in self.trace: 
            pygame.draw.circle(self.screen, (0,255,25), p, 1,0)


        pygame.display.flip()
        self.clock.tick(self.fps)

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
        sys.exit()