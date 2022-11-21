
class Pheromone:
    DEFAULT_INCREASE_AMOUNT = 0.05
    DEFAULT_DECREASE_AMOUNT = 0.0005
    MAXIMUM_AMOUNT = 5
    MAXIMUM_STEPS = 20

    x: int
    y: int
    weight: float

    def __init__(self, x: int, y: int, weight: float = DEFAULT_INCREASE_AMOUNT):
        self.x = x
        self.y = y
        self.weight = weight


    def decrease_intensity(self, amount: float = DEFAULT_DECREASE_AMOUNT):
        decreased_amount = self.weight - amount
        self.weight = decreased_amount if decreased_amount >= 0 else 0


    def increase_intensity(self, amount: float = DEFAULT_INCREASE_AMOUNT):
        sum_amount = self.weight + amount
        self.weight = self.MAXIMUM_AMOUNT if sum_amount > self.MAXIMUM_AMOUNT else sum_amount
