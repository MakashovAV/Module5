# Цель: понять как работают базовые магические методы на практике.
# Задача "Магические здания":

class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей:{self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
