import pygame
from typing import Mapping, Tuple
from models.pheromone import Pheromone
from sprites.custom_sprite import CustomSprite


class PheromoneSprite(CustomSprite):

    pheromones_layer: Mapping[Tuple[int, int], Pheromone]
    
    def __init__(self, width: int, height: int, scale: int, pheromones: Mapping[Tuple[int, int], Pheromone]):
        super().__init__(width=width, height=height, scale=scale, size = 0.2)

        self.pheromones_layer = pheromones

        self.image = pygame.Surface([width * scale, height * scale])
        self.rect = self.image.get_rect()
    

    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")

        for pheronome in self.pheromones_layer.values():
            pygame.draw.rect(self.image, "purple", (self.scale * pheronome.x, self.scale * pheronome.y, self.scale*self.size, self.scale*self.size))