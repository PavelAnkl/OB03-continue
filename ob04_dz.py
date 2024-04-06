# Абстрактный класс для оружия
from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Класс Бойца
class Fighter:
    def __init__(self, weapon):
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon

    def attack(self):
        print(self.weapon.attack())

# Класс Монстров
class Monster:
    def __init__(self, health):
        self.health = health

    def is_defeated(self):
        return self.health <= 0

# Механизм боя
def battle(fighter, monster):
    while not monster.is_defeated():
        action = input("Выберите действие: атаковать или сменить оружие: ")
        if action == "атаковать":
            print(fighter.attack())
            monster.health -= 10  # Простая логика уменьшения здоровья монстра
        elif action == "сменить оружие":
            new_weapon_name = input("Введите новое оружие (меч или лук): ")
            if new_weapon_name == "меч":
                fighter.change_weapon(Sword())
            elif new_weapon_name == "лук":
                fighter.change_weapon(Bow())
            else:
                print("Неверное оружие")
    print("Монстр побежден!")

# Пример использования
# Инициализация бойца с мечом
fighter = Fighter(Sword())
# Инициализация монстра
monster = Monster(health=30)

# Запуск боя
battle(fighter, monster)
