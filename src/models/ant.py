
from typing import Tuple, List, Mapping

from models.colony import Colony
from models.food import Food
from models.pheromone import Pheromone

from states.ant_fsm import AntFSM

class Ant:
    x: int
    y: int
    age: int
    fsm: AntFSM
    colony: Colony
    resources: int
    maximum_resources: int = 2
    game_grid: Tuple[int, int]
    pheromones: Mapping[Tuple[int, int], Pheromone]

    def __init__(self, colony: Colony, pheromone_layer: Mapping[Tuple[int, int], Pheromone], game_grid: Tuple[int, int]) -> None:
        self.colony = colony
        self.x = colony.x
        self.y = colony.y
        self.age = 0
        self.fsm = AntFSM()
        self.resources = 0
        self.game_grid = game_grid
        self.pheromones = pheromone_layer
    
    def walk(self, vector: Tuple[int, int]):
        self.x = self.x + vector[0]
        self.y = self.y + vector[1]

        # constraint ant inside game grid (world)
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > self.game_grid[0]:
            self.x = self.game_grid[0]
        if self.y > self.game_grid[1]:
            self.y = self.game_grid[1]

    def update(self):
        self.fsm.update(ant=self)

    def eat(self, food: Food):
        self.resources += food.pick(self.maximum_resources - self.resources)
        self.fsm.event("found_food", self)
    
    def release_pheromone(self, amount: float = Pheromone.DEFAULT_INCREASE_AMOUNT):
        curr_position: Tuple[int, int] = (self.x, self.y)

        # create if does not exist
        if curr_position not in self.pheromones:
            self.pheromones[curr_position] = Pheromone(x = self.x, y = self.y, weight=0)
        
        # add weight
        self.pheromones[curr_position].increase_intensity(amount=amount)
    
    def search_pheromones(self) -> Tuple[int, int] or None:

        # get coordinates around ant position
        coordinates: List[Tuple[int, int]] = [(self.x+i, self.y+j) for i in range(-1, 2) for j in range(-1, 2)]

        # get pheromones in the coordinates around
        close_pheromones: List[Pheromone] = [self.pheromones[coordinate] for coordinate in coordinates if coordinate in self.pheromones]

        if len(close_pheromones) == 0:
            return None

        # get the one with the highest weight
        higher_pheromone = max(close_pheromones, key=lambda pheromone: pheromone.weight)


        # check if it is not the last pheromone
        curr_position_pheromone = self.pheromones.get((self.x, self.y), None)
        if curr_position_pheromone is not None:
            if curr_position_pheromone.weight == higher_pheromone.weight:
                self.pheromones[(self.x, self.y)].decrease_intensity(amount = Pheromone.DEFAULT_DECREASE_AMOUNT)
                return None


        # get the vector the ant needs to move to
        return (higher_pheromone.x - self.x, higher_pheromone.y - self.y)