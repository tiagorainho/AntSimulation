
class Food:
    x: int
    y: int
    resources: int

    def __init__(self, x: int, y: int, resources: int = 50):
        self.x = x
        self.y = y
        self.resources = resources
    
    def pick(self, amount: int) -> int:
        to_remove: int = self.resources
        if self.resources > amount:
            to_remove = amount
        
        self.resources -= to_remove
        return to_remove