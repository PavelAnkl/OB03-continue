class Teacher():
    def teach(self):
        print ('преподаватель учит')

# Создаем класс School с функцией init, внутри которой будет еще одна функция — start_lesson (начать урок).
class School():
    def init(self, new_teacher):
        self.teacher = new_teacher
    def start_lesson():
        self.teacher.teach()

my_teacher = Teacher()
# my_teacher.teach()
my_school = School(my_teacher)