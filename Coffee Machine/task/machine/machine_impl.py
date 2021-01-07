from recipe_manager import coffee_recipes


class CoffeeMachine:
    # Actions
    ACTION_BUY = 'buy'
    ACTION_FILL = 'fill'
    ACTION_TAKE = 'take'
    ACTION_REMAINING = 'remaining'
    ACTION_BACK = 'back'
    ACTION_EXIT = 'exit'

    recipes = coffee_recipes

    def __init__(self, water: int, milk: int, beans: int, cups: int, money: int) -> None:
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def __str__(self):
        return f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
{self.money} of money"""

    def process_recipe(self, recipe: int):
        """Makes a coffee type and transact price"""

        recipe = CoffeeMachine.recipes.get_recipe(recipe)

        if (self.water - recipe.water) < 0:
            print('Sorry, not enough water!')
            return

        if (self.milk - recipe.milk) < 0:
            print('Sorry, not enough milk!')
            return

        if (self.beans - recipe.beans) < 0:
            print('Sorry, not enough coffee beans!')
            return

        if self.cups == 0:
            print('Sorry, not enough coffee disposable cups!')
            return

        print('I have enough resources, making you a coffee!')

        # Charging
        self.water -= recipe.water
        self.milk -= recipe.milk
        self.beans -= recipe.beans
        self.money += recipe.cost
        self.cups -= 1

    def run_action(self, action: str) -> None:
        if action == CoffeeMachine.ACTION_BUY:
            self.action_buy()
        if action == CoffeeMachine.ACTION_FILL:
            self.action_fill()
        if action == CoffeeMachine.ACTION_TAKE:
            self.action_take()
        if action == CoffeeMachine.ACTION_REMAINING:
            self.action_remains()

    def run(self) -> None:
        # Start
        while True:
            print('\nWrite action (buy, fill, take, remaining, exit):')
            action = input().strip()

            if action == CoffeeMachine.ACTION_EXIT:
                break

            print()
            self.run_action(action)

    def action_buy(self) -> None:
        available = []

        for key, recipe in CoffeeMachine.recipes.recipes.items():
            available.append(f'{key} - {recipe.name.lower()}')

        available.append('back - to main menu:')

        print('What do you want to buy? {}'.format(', '.join(available)))
        coffee_recipe = input().strip()

        if coffee_recipe == CoffeeMachine.ACTION_BACK:
            return

        self.process_recipe(int(coffee_recipe))

    def action_fill(self):
        """Fill ingredients into machine"""
        print('Write how many ml of water do you want to add:')
        self.water += int(input().strip())

        print('Write how many ml of milk do you want to add:')
        self.milk += int(input().strip())

        print('Write how many grams of coffee beans do you want to add:')
        self.beans += int(input().strip())

        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input().strip())

    def action_take(self) -> None:
        """Takes all money from machine"""
        print(f'I gave you ${self.money}')
        self.money = 0

    def action_remains(self) -> None:
        print(self)
