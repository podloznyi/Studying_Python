# 2. Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде
# списка объектов `Student` также реализованного в виде соответствующего класса.
# В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь
# атрибуты `name`, `age`, `grades`), а так же необходимый набор методов экземпляра для
# работы с этими экземплярами.
#
# Наследование здесь не понадобится.
class Group:
    def __init__(self, lstStudents):
        self.lstStudents = lstStudents

    def getGroupList(self):
        return self.lstStudents

    def getGroupSize(self):
        return len(self.lstStudents)

    def getNames(self):
        return [x.getName() for x in self.lstStudents]

    def getAvrGroupGrade(self):
        temp = [x.getAverageGrade() for x in self.lstStudents]
        return sum(temp) / len(temp)

class Student:
    def __init__(self, _name, _age, _grades):
            self._name = _name
            self._age = _age
            self._grades = _grades

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def getGrades(self):
        return self._grades

    def getAverageGrade(self):
        return sum(self._grades)/len(self._grades)