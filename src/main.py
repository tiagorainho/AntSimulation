from game.game import Game
from game.ant_game import AntGame

SCALE = 2
import pygame

if __name__ == '__main__':
    # get width and height from pygame
    pygame.init()
    info = pygame.display.Info()
    width, height = info.current_w,info.current_h

    # decrease a bit the height because of the top bar (otherwise it would hide the bottom area)
    height -= 30

    # create and start the simulation
    game: Game = AntGame(width=width, height=height, scale = SCALE)
    game.start()
