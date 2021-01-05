# Write your code here

print('Write how many cups of coffee you will need:')

cups = int(input().strip())

print(f'For {cups} cups of coffee you will need:')


def calculate_water(cups_qty: int) -> int:
    return 200 * cups_qty


def calculate_milk(cups_qty: int) -> int:
    return 50 * cups_qty


def calculate_beans(cups_qty: int) -> int:
    return 15 * cups_qty


print('{water} ml of water'.format(water=calculate_water(cups)))
print('{milk} ml of milk'.format(milk=calculate_milk(cups)))
print('{beans} g of coffee beans'.format(beans=calculate_beans(cups)))
