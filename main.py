# class Report():
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#     def docPrinter(self):
#         print(f"сформирован отчет - {self.title} - {self.content}")

from abc import ABC, abstractmethod

class Formatted(ABC):
    @abstractmethod
    def format(self, report):
        pass

class TextFormatted(Formatted):
    def format(self, report):
        print()
        print()

class HtmlFormatted(Formatted):
    def format(self, report):
        print()
        print()

class Report():
    def __init__(self, title, content, formatted):
        self.title = title
        self.content = content
        self.formatted = formatted

