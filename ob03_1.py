class Engine():
    def start(self):
        print('Двигатель запущен')
    def stop(self):
        print('Двигатель остановлен')

# Создаем отдельный класс Car с функцией def init:

class Car():
    def __init__(self):
        # Внутри def init создаем объект класса self.engine

        self.engine = Engine()
        # Engine — название класса, engine — переменная, в которую сохраняется объект класса.
        # Получается, что сейчас был создан объект класса внутри другого класса — настроена строгая взаимосвязь.
        # Создаем функцию start:
    def start(self):
    # Вызываем функцию start через объект класса:
        self.engine.start()
    def stop(self):
        self.engine.stop()

my_Car = Car()
# Попробуем использовать функцию start
my_Car.start()
my_Car.stop()