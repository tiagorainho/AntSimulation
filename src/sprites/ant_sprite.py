import pygame
from typing import List
from models.ant import Ant
from sprites.custom_sprite import CustomSprite
from states.ant_fsm import ReturnColony


class AntSprite(CustomSprite):

    ant: Ant
    
    def __init__(self, width: int, height: int, scale: int, ant: Ant):
        super().__init__(width=width, height=height, scale=scale, size = 3)
        self.ant = ant

        self.image = pygame.Surface([scale, scale])
        self.rect = self.image.get_rect()
    

    def update(self):
        color = "green" if isinstance(self.ant.fsm.current, ReturnColony) else "red"
        self.image.fill(color = color)
        
        self.rect.x = self.ant.x * self.scale
        self.rect.y = self.ant.y * self.scale