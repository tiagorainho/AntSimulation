
from states.fsm import FSM, State, Transition
from random import randint

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

        # compute vector to colony
        vector = [ant.colony.x - ant.x, ant.colony.y - ant.y]

        # normalize vector
        if vector[0] != 0:
            vector[0] = 1 if vector[0] > 0 else -1

        if vector[1] != 0:
            vector[1] = 1 if vector[1] > 0 else -1

        ant.release_pheromone()
        ant.walk(vector = vector)
        