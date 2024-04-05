class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        print("Издает звук")
    def eat(self):
        print(f"{self.name} ест")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} чирикает")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} издает звук, специфичный для млекопитающих")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")
    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member.name} добавлен в зоопарк")

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        print(f"Смотритель {self.name} кормит {animal.name}")

class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f"Ветеринар {self.name} лечит {animal.name}")


# Пример использования
zoo = Zoo()

# Создаем животных
parrot = Bird("Попугай Кеша", 2)
dog = Mammal("Собака Барбос", 4)
snake = Reptile("Змея Сссергей", 3)

# Создаем сотрудников
keeper = ZooKeeper("Иван")
vet = Veterinarian("Алиса")

# Добавляем животных и сотрудников в зоопарк
zoo.add_animal(parrot)
zoo.add_animal(dog)
zoo.add_animal(snake)

zoo.add_staff(keeper)
zoo.add_staff(vet)

# Пример полиморфизма
animal_sound(zoo.animals)

# Смотритель кормит животное
keeper.feed_animal(dog)

# Ветеринар лечит животное
vet.heal_animal(snake)


