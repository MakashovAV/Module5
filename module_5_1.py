# Цель: применить на практике знания о классах, объектах и их атрибутах.
# Задача "Developer - не только разработчик":

class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors and new_floor > 0:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 10)
h1.go_to(0)
h2.go_to(10)
h3.go_to(3)
