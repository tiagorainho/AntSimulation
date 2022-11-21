from typing import DefaultDict
from collections import defaultdict

import pygame

class Game:
    clock: pygame.time.Clock
    fps: int
    display: pygame.display
    screen: pygame.Surface
    running: bool
    sprites: DefaultDict[str, pygame.sprite.Group]
    scale: int
    height: int
    width: int
    scale: int

    
    def __init__(self, height: int, width: int, scale: int):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.scale = scale
        self.height = height*self.scale
        self.width = width*self.scale
        self.display = pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.Surface((self.width, self.height))
        self.fps = 20

        self.sprites = defaultdict(pygame.sprite.Group)
        
        pygame.mixer.init()
        pygame.mixer.stop()

    def start(self):
        self.run(self.update)

    def run(self, update_function):
        self.running = True

        while self.running:

            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    exit()
                
            update_function(events)

            # render window
            self.screen.fill("white")
            self.render_sprites()

            # update display
            pygame.Surface.blit(self.display, self.screen, (0,0))
            pygame.display.flip()

            self.clock.tick(self.fps)
        
    def render_sprites(self):
        for group in self.sprites.values():
            group.update()
            group.draw(self.screen)