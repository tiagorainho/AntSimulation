import pygame
from typing import List
from models.ant import Ant
from sprites.custom_sprite import CustomSprite
from states.ant_fsm import ReturnColony


class AntSprite(CustomSprite):

    ants: List[Ant]
    
    def __init__(self, width: int, height: int, scale: int, ants: List[Ant]):
        super().__init__(width=width, height=height, scale=scale)
        self.ants = ants

        self.image = pygame.Surface([width * scale, height * scale])
        self.rect = self.image.get_rect()
    

    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")

        for ant in self.ants:
            color = "red"
            if isinstance(ant.fsm.current, ReturnColony):
                color = "green"
            pygame.draw.rect(self.image, color, (self.scale * ant.x, self.scale * ant.y, self.scale, self.scale))


