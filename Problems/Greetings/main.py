class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self) -> str:
        return f'Hello, I am {self.name}!'


input_name = input()

man = Person(input_name)

print(man.greet())
