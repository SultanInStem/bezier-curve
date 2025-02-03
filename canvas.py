import pygame
from globals import SCREEN_SIZE
class Canvas: 
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.running = True

        pygame.display.set_caption("Bezier Curve")

    def handle_events(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 

    def update(self): 
        pass 

    def render(self): 
        pass

    def run(self): 
        while(self.running): 
            self.handle_events()
            self.update()
            self.render()