class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars: int, cents: int) -> None:
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars: int, deposit_cents: int):
        self.dollars += deposit_dollars

        all_cents = deposit_cents + self.cents

        self.dollars += all_cents // 100
        self.cents = all_cents % 100
