class Animal:
    def __init__(self, species, color, sound):
        self.species = species
        self.color = color
        self.sound = sound

    def make_sound(self):
        print(f'{self.color} {self.species} says {self.sound}')

    def eat(self, food):
        print(f'{self.species} eats {food}')

    def sleep(self):
        print(f'{self.species} is sleeping')

class Cow(Animal):
    def __init__(self):
        super().__init__('cow', 'black', 'moo')

    def produce_milk(self):
        print(f'{self.species} is producing milk')

class Chicken(Animal):
    def __init__(self):
        super().__init__('chicken', 'yellow', 'cluck')

    def lay_egg(self):
        print(f'{self.species} is laying egg')

class Sheep(Animal):
    def __init__(self):
        super().__init__('sheep', 'brown', "baa")