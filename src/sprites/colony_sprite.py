import pygame

from typing import List
from models.colony import Colony
from sprites.custom_sprite import CustomSprite


class ColonySprite(CustomSprite):

    colonies: List[Colony]
    
    def __init__(self, width: int, height: int, scale: int, colony: List[Colony]):
        super().__init__(width=width, height=height, scale=scale, size = 5)

        self.colonies = colony

        self.image = pygame.Surface([width * scale, height * scale])
        self.rect = self.image.get_rect()
    

    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")
        
        for colony in self.colonies:
            pygame.draw.rect(self.image, "purple", (self.scale * colony.x, self.scale * colony.y, self.scale*self.size, self.scale*self.size))