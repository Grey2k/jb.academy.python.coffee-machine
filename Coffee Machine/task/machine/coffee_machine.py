# Write your code here
WATER_RECIPE = 200
MILK_RECIPE = 50
BEANS_RECIPE = 15


def calculate_water(cups_qty: int) -> int:
    return WATER_RECIPE * cups_qty


def calculate_milk(cups_qty: int) -> int:
    return MILK_RECIPE * cups_qty


def calculate_beans(cups_qty: int) -> int:
    return BEANS_RECIPE * cups_qty


def calculate_cups(water_qry: int, milk_qty: int, beans_qty: int) -> int:
    water_cups = water_qry // WATER_RECIPE
    milk_cups = milk_qty // MILK_RECIPE
    beans_cups = beans_qty // BEANS_RECIPE

    cups_qty = min(water_cups, milk_cups, beans_cups)
    return cups_qty


print('Write how many ml of water the coffee machine has:')
water = int(input().strip())

print('Write how many ml of milk the coffee machine has:')
milk = int(input().strip())

print('Write how many grams of coffee beans the coffee machine has:')
beans = int(input().strip())

print('Write how many cups of coffee you will need:')
cups = int(input().strip())

available = calculate_cups(water, milk, beans)

if cups > available:
    print(f'No, I can make only {available} cups of coffee')
else:
    print(
        'Yes, I can make that amount of coffee{}'.format(
            ' (and even {extra} more than that)'.format(extra=available - cups) if cups < available else ''))
