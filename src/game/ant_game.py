
import pygame

from typing import List, Mapping, Tuple
from random import randint

from game.game import Game
from models.ant import Ant
from models.food import Food
from models.colony import Colony
from models.pheromone import Pheromone

from sprites.ant_sprite import AntSprite
from sprites.food_sprite import FoodSprite
from sprites.colony_sprite import ColonySprite
from sprites.pheromone_sprite import PheromoneSprite


INITIAL_NUMBER_OF_ANTS = 200
NUMBER_OF_FOOD = 50
NUMBER_OF_COLONIES = 20


class AntGame(Game):
    food: List[Food]
    colony: List[Colony]
    ants: List[Ant]
    pheromones: Mapping[Tuple[int, int], Pheromone]
    game_grid: Tuple[int, int]

    def __init__(self, width: int, height: int, scale: int):
        self.game_grid = (width/scale, height/scale)
        super().__init__(height = self.game_grid[1], width = self.game_grid[0], scale = scale)

        # create colonies
        self.colony = [Colony(randint(0, self.game_grid[0]), randint(0, self.game_grid[1])) for _ in range(NUMBER_OF_COLONIES)]

        # create ants
        self.ants = []
        self.pheromones = dict()
        for c in self.colony:
            self.ants.extend([Ant(colony=c, pheromone_layer=self.pheromones, game_grid=self.game_grid) for _ in range(INITIAL_NUMBER_OF_ANTS)])

        # create food
        self.food = [Food(randint(0, self.game_grid[0]), randint(0, self.game_grid[1])) for _ in range(NUMBER_OF_FOOD)]
        

        # add sprites
        self.all_sprites.add(
            AntSprite(width=width, height=height, scale=scale, ants=self.ants)
        )

        self.all_sprites.add(
            PheromoneSprite(width=width, height=height, scale=scale, pheromones=self.pheromones)
        )

        self.all_sprites.add(
            FoodSprite(width=width, height=height, scale=scale, food=self.food)
        )

        self.all_sprites.add(
            ColonySprite(width=width, height=height, scale=scale, colony=self.colony)
        )


    def update(self, events: List[pygame.event.Event]):
        """
        Game logic
        """

        # FAZER: press scape to switch simulation settings
        # handle events
        # for event in events:


        # update ant state
        for ant in self.ants:
            ant.update()
        
        # check if ants can eat
        for ant in self.ants:
            for f in self.food:
                if ant.x == f.x and ant.y == f.y:
                    ant.eat(f)

        # remove food without resources
        for f in self.food:
            if f.resources == 0:
                self.food.remove(f)
                self.food.append(Food(randint(0, self.game_grid[0]), randint(0, self.game_grid[1])))

        # decay pheromones
        for pheromone in self.pheromones.values():
            pheromone.decrease_intensity()

        for pheromone in self.pheromones.copy().values():
            # remove pheromones without trail
            if pheromone.weight == 0:
                del self.pheromones[(pheromone.x, pheromone.y)]
        
        
        