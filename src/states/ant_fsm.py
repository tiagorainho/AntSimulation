
from states.fsm import FSM, State, Transition
from random import randint

from models.pheromone import Pheromone
from math import dist

class AntFSM(FSM):

    def __init__(self):
        forage = Forage()
        return_colony = ReturnColony()

        states = [forage, return_colony]
        transitions = {
            "reach_colony": Transition(return_colony, forage),
            "found_food": Transition(forage, return_colony)
        }

        super().__init__(states, transitions)

    def update(self, ant):
        self.current.update(ant)


class Forage(State):

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, ant):
        ant.steps_from_food = 0

        # get cells around to check for feromones
        vector = ant.search_pheromones()
        
        # search in a random direction
        if vector == None:
            vector = (randint(-1, 1), randint(-1, 1))

        ant.walk(vector = vector)


class ReturnColony(State):

    def __init__(self) -> None:
        super().__init__(self.__class__.__name__)

    def update(self, ant):
        if ant.x == ant.colony.x and ant.y == ant.colony.y:
            ant.fsm.event("reach_colony", ant)
            return
        
        ant.steps_from_food += 1

        # compute vector to colony
        vector = [ant.colony.x - ant.x, ant.colony.y - ant.y]

        delta_x = 0
        delta_y = 0

        # normalize delta x and delta y
        if vector[0] != 0:
            delta_x = 1 if vector[0] > 0 else -1

        if vector[1] != 0:
            delta_y = 1 if vector[1] > 0 else -1

        adjacent_coordinates = [
            (ant.x + delta_x, ant.y),
            (ant.x + delta_x, ant.y + delta_y),
            (ant.x, ant.y + delta_y)
        ]

        # get colony vector normalized
        colony_vector_length = dist((ant.colony.x, ant.colony.y), (ant.x, ant.y))
        colony_vector_normalized = (vector[0]/colony_vector_length, vector[1]/colony_vector_length)
        normalized_to_colony_vector = (ant.x + colony_vector_normalized[0], ant.y + colony_vector_normalized[1])

        # compute closest coordinate to the colony vector normalized
        closest_coordinate = min(adjacent_coordinates, key=lambda possible_closest_coord: dist(normalized_to_colony_vector, possible_closest_coord))

        # convert the coordinate to move to, to a vector for the ant to move
        normalized_vector = (closest_coordinate[0] - ant.x, closest_coordinate[1] - ant.y)

        # release pheromones while returning home
        ant.release_pheromone(amount = Pheromone.DEFAULT_INCREASE_AMOUNT/ant.steps_from_food)
        
        # pheromone release alternative functions

        # ant.release_pheromone(amount = Pheromone.DEFAULT_INCREASE_AMOUNT)
        # ant.release_pheromone(amount = pow(10*ant.steps_from_food, -2) + Pheromone.DEFAULT_INCREASE_AMOUNT)
        # ant.release_pheromone(amount = Pheromone.MAXIMUM_AMOUNT-Pheromone.MAXIMUM_AMOUNT * (ant.steps_from_food/Pheromone.MAXIMUM_STEPS))

        ant.walk(vector = normalized_vector)