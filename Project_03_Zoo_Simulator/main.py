class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping .....Zzzzz")
class Lion(Animal):
    def roar(self):
        print(f"{self.name} lets out a loud ROAR! 🦁")
class Bird(Animal):
    def sleep(self):
        print(f"{self.name} is sleeping in a high nest 🪹")
    def fly(self):
        print(f"{self.name} is soaring through the sky!! 🦅")
class Elephant(Animal):
    def sleep(self):
        print(f"{self.name} is sleeping on the ground !!!")

simba = Lion("Simba", "Lion")
black_bird = Bird("Tweety", "Bird")
dumbo = Elephant("Dumbo", "Elephant")

zoo = [simba, black_bird, dumbo]
for animal in zoo:
    animal.sleep()

simba.roar()
black_bird.fly()