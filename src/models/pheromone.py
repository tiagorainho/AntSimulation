
class Pheromone:
    DEFAULT_INCREASE_AMOUNT = 0.1
    DEFAULT_DECREASE_AMOUNT = 0.005

    x: int
    y: int
    weight: float

    def __init__(self, x: int, y: int, weight: float = DEFAULT_INCREASE_AMOUNT):
        self.x = x
        self.y = y
        self.weight = weight


    def decrease_intensity(self, amount: float = DEFAULT_DECREASE_AMOUNT):
        to_remove: float = self.weight
        if self.weight > amount:
            to_remove = amount
        
        self.weight -= to_remove


    def increase_intensity(self, amount: float = DEFAULT_INCREASE_AMOUNT):
        self.weight += amount
