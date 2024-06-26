# ZOO
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return ({"self.name, self.species"})

class Mammal(Animal):
    def __init__(self, name, species, num_legs):
        super().__init__(name, species)
        self.num_legs = num_legs

    def make_sound(self):
        return ({"self.name, self.species"})

class Bird(Animal):
    def __init__(self, name, species, can_fly):
        super().__init__(name, species)
        self.can_fly = can_fly

    def make_sound(self):
        return  ("{self.name, self.species}")


elephant = mammal("Elephant", "African Elephant", num_legs=4)
sparrow = bird("Sparrow", "House Sparrow", can_fly=True)

# Demonstrate make_sound() method

elephant.make_sound()
sparrow.make_sound()
