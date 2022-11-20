
import pygame

class CustomSprite(pygame.sprite.Sprite):
    height: int
    width: int
    scale: int
    size: float

    def __init__(self, width: int, height: int, scale: int, size: float = 1):
        pygame.sprite.Sprite.__init__(self)

        self.height = height
        self.width = width
        self.scale = scale
        self.size = size