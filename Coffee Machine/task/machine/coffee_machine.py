import machine_check

# Constants
ACTION_BUY = 'buy'
ACTION_FILL = 'fill'
ACTION_TAKE = 'take'
ACTION_REMAINING = 'remaining'
ACTION_BACK = 'back'
ACTION_EXIT = 'exit'

TYPE_ESPRESSO = 1
TYPE_LATTE = 2
TYPE_CAPPUCCINO = 3

# Initial ingredients
water = 400
milk = 540
beans = 120
cups = 9
money = 550


def buy_coffee(type_name: int):
    """Makes a coffee type and transact price"""

    global water
    global milk
    global beans
    global cups
    global money

    water_charge = 0
    milk_charge = 0
    beans_charge = 0
    money_charge = 0

    if type_name == TYPE_ESPRESSO:
        water_charge = 250
        beans_charge = 16
        money_charge = 4
    if type_name == TYPE_LATTE:
        water_charge = 350
        milk_charge = 75
        beans_charge = 20
        money_charge = 7
    if type_name == TYPE_CAPPUCCINO:
        water_charge = 200
        milk_charge = 100
        beans_charge = 12
        money_charge = 6

    if (water - water_charge) < 0:
        print('Sorry, not enough water!')
        return

    if (milk - milk_charge) < 0:
        print('Sorry, not enough milk!')
        return

    if (beans - beans_charge) < 0:
        print('Sorry, not enough coffee beans!')
        return

    if cups == 0:
        print('Sorry, not enough coffee disposable cups!')
        return

    print('I have enough resources, making you a coffee!')

    # Charging
    water -= water_charge
    milk -= milk_charge
    beans -= beans_charge
    money += money_charge
    cups -= 1


def action_buy() -> None:
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    coffee_type = input().strip()

    if coffee_type == ACTION_BACK:
        return

    buy_coffee(int(coffee_type))


def action_fill():
    """Fill ingredients into machine"""

    global water
    global milk
    global beans
    global cups

    print('Write how many ml of water do you want to add:')
    water += int(input().strip())

    print('Write how many ml of milk do you want to add:')
    milk += int(input().strip())

    print('Write how many grams of coffee beans do you want to add:')
    beans += int(input().strip())

    print('Write how many disposable cups of coffee do you want to add:')
    cups += int(input().strip())


def action_take():
    """Takes all money from machine"""

    global money

    print(f'I gave you ${money}')
    money = 0


def run_action(action_name: str) -> None:
    if action_name == ACTION_BUY:
        action_buy()
    if action_name == ACTION_FILL:
        action_fill()
    if action_name == ACTION_TAKE:
        action_take()
    if action_name == ACTION_REMAINING:
        machine_check.run(water, milk, beans, cups, money)


# Start
while True:
    print('\nWrite action (buy, fill, take, remaining, exit):')
    action = input().strip()

    if action == ACTION_EXIT:
        break

    print()
    run_action(action)
