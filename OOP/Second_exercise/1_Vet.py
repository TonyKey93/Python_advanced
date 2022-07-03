class Vet:
    animals = []
    space = 5
    def __init__(self, name):
        self.name = name

    def register_animal(self, animal_name):
        if len(Vet.animals) >= Vet.space:
            return "Not enough space"
        self.animals.append(animal_name)
        Vet.animals.append(animal_name)
        

