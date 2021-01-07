from typing import Dict

from coffee_recipe import CoffeeRecipe


class RecipeManager:
    def __init__(self, recipes: Dict[int, CoffeeRecipe]) -> None:
        self.recipes = recipes

    def get_recipe(self, index: int) -> 'CoffeeRecipe':
        return self.recipes.get(index)


coffee_recipes = RecipeManager({
    1: CoffeeRecipe(name='Espresso', water=250, beans=16, cost=4),
    2: CoffeeRecipe(name='Latte', water=350, milk=75, beans=20, cost=7),
    3: CoffeeRecipe(name='Cappuccino', water=200, milk=100, beans=12, cost=6)
})
