
from states.fsm import FSM, State, Transition
from random import randint

from models.pheromone import Pheromone

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

        # normalize vector
        if vector[0] != 0:
            vector[0] = 1 if vector[0] > 0 else -1

        if vector[1] != 0:
            vector[1] = 1 if vector[1] > 0 else -1

        # release pheromones while returning home
        ant.release_pheromone(amount = Pheromone.DEFAULT_INCREASE_AMOUNT/ant.steps_from_food)
        
        # pheromone release alternative functions
        # ant.release_pheromone(amount = Pheromone.DEFAULT_INCREASE_AMOUNT)
        # ant.release_pheromone(amount = pow(10*ant.steps_from_food, -2) + Pheromone.DEFAULT_INCREASE_AMOUNT)
        # ant.release_pheromone(amount = Pheromone.MAXIMUM_AMOUNT-Pheromone.MAXIMUM_AMOUNT * (ant.steps_from_food/Pheromone.MAXIMUM_STEPS))

        ant.walk(vector = vector)
        