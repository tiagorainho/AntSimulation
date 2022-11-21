import pygame
from typing import List
from models.food import Food
from sprites.custom_sprite import CustomSprite


class FoodSprite(CustomSprite):

    food: List[Food]
    
    def __init__(self, width: int, height: int, scale: int, food: List[Food]):
        super().__init__(width=width, height=height, scale=scale, size=3)

        self.food = food

        self.image = pygame.Surface([width * scale, height * scale])
        self.rect = self.image.get_rect()
    

    def update(self):
        self.image.fill("white")
        self.image.set_colorkey("white")

        for f in self.food:
            pygame.draw.rect(self.image, "green", (self.scale * f.x, self.scale * f.y, self.scale*self.size, self.scale*self.size))