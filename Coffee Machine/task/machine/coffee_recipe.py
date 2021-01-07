class CoffeeRecipe:
    def __init__(self, name: str, water: int, beans: int, cost: int, milk: int = 0) -> None:
        self.name = name
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost
