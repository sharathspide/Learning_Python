class animal:
    def __init__(self, animal: str):
        self.animal = animal

    def sound(self):
        print(f"the animal {self.animal} is making sound")

class dog(animal):
    def __init__(self, animal: str):
        super().__init__(animal)

    def sound(self):
        print(f"This animal is dog and hence bark")

    def bark(self):
        print(f"the dog named {self.animal} is barking...")

class bommarian(dog):
    def __init__(self, animal: str, name:str):
        super().__init__(animal)
        self.name = name

    def bark(self):
        print("the bommarian dog is barking...")


dogs = animal("dog")
dogs.sound()

# nithi = dog("nithi")
# nithi.sound()
# nithi.bark()

nithi = bommarian("pet-dog", "nithi")
nithi.bark()