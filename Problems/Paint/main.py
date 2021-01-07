class House:
    def __init__(self, floors):
        self.floors = floors
        self.color = None

    # create the method here
    def paint(self, color: str) -> None:
        self.color = color
