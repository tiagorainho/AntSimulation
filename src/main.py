from game.game import Game
from game.ant_game import AntGame

HEIGHT = 600
WIDTH = 800
SCALE = 5

if __name__ == '__main__':
    game: Game = AntGame(height = HEIGHT, width = WIDTH, scale = SCALE)
    game.start()
