# TODO 11.2 Polymorphism
# Type in the mammal class from program 11-9    lines 1 - 22


class Mammal:
    def __init__(self, species):
        self.species = species

    def show_species(self):
        print("I am a", self.species)

    def make_sound(self):
        print("Grrr!")

# create a Mouse class as a sub class of the mammal class following the Dog example


class Mouse(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Mouse")

    def make_sound(self):
        print("Squeak!")

# create a Bird class as a sub class of the mammal class following the Cat Example


class Bird(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Bird")

    def make_sound(self):
        print("Tweet!")

# Follow the example in program 11-10 (no need to import, use main2 instead of main
# because there is already a main on this page) use the Mouse and Bird class that you created


def main2():
    mammal = Mammal("Regular animal")
    mouse = Mouse()
    bird = Bird()

    print("Here are some animals and")
    print("the sound they make.")
    print("--------------------------")
    show_mammal_info(mammal)
    print()
    show_mammal_info(mouse)
    print()
    show_mammal_info(bird)


def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()


main2()
