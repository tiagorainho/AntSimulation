from game.game import Game
from game.ant_game import AntGame

import cProfile

DEBUG: bool = False

SCALE = 3
import pygame
import atexit
import pstats
import io

pr: cProfile.Profile


def exit_handler():
    if not DEBUG: return
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('tottime')
    ps.print_stats()

    with open('log.txt', 'w+') as f:
        f.write(s.getvalue())


if __name__ == '__main__':

    if DEBUG:
        atexit.register(exit_handler)
        pr = cProfile.Profile()
        pr.enable()

    # get width and height from pygame
    pygame.init()
    info = pygame.display.Info()
    width, height = info.current_w,info.current_h

    # decrease a bit the height because of the top bar (otherwise it would hide the bottom area)
    height -= 30

    # create and start the simulation
    game: Game = AntGame(width=width, height=height, scale = SCALE)
    game.start()

    if DEBUG:
        pr.disable()
