# Определение класса Author
class Author():
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

# Исправленный класс Book
class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info_book(self):  # Добавлен self в качестве параметра
        print(f'{self.title} - {self.author.name}')  # Исправлен отступ

# Создание объекта класса Author
author = Author("Лев Толстой", "Русский")

# Создание объекта класса Book
book = Book('Война и мир', author)

# Вызов метода get_info_book
book.get_info_book()

# Вывод имени автора
print(author.name)