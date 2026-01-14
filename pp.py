class birds():
    def __init__(self,sound):
        self.sound1 = sound

    def sound (self):
        print(f"{self.__class__.__name__} says : {self.sound}")

class Sparrow(birds):
    def sound(self):
        print(f"Sparrow says : {self.sound1}")

class Crow(birds):
    def sound (self):
        print(f"Crow says : {self.sound1}")

class Pigeon(birds):
    def sound (self):
        print(f"Pigeon says : {self.sound1}")

class Parrot(birds):
    def sound (self):
        print(f"Parrot says : {self.sound1}")

class Robin(birds):
    def sound (self):
        print(f"Robin says : {self.sound1}")

Birds = [
    Robin("cheep cheep"),
    Parrot("squawk"),
    Pigeon("coo coo"),
    Crow("caw caw"),
    Sparrow("chirp chirp")
]


for i in range(2):
    for Bird in Birds:
        Bird.sound()