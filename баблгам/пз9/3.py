from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name
        self.value = None

    def __get__(self, instance, owner):
        if self.value is None:
            raise AttributeError('Атрибут не найден')
        return self.value

    def __set__(self, instance, value):
        self.validate(value)
        self.value = value
    @abstractmethod
    def validate(self):
        pass



class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, obj):
        if not isinstance(obj, int or float):
            raise TypeError(f'Устанавливаемое значение должно быть числом')
        if obj < self.minvalue:
            raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if obj > self.maxvalue:
            raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, obj):
        if not isinstance(obj, str):
            raise TypeError(f'Устанавливаемое значение должно быть строкой')
        if len(obj) < self.minsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if len(obj) > self.maxsize:
            raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if self.predicate is False:
            raise ValueError(f'Устанавливаемая строка не удовлетворяет дополнительным условиям')



class Student:
    age = Number(18, 99)


student = Student()
student.age = 19
print(student.age)

class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = '19'
except TypeError as error:
    print(error)

class Student:
    age = Number(18, 99)

try:
    student = Student()
    student.age = 16
except ValueError as error:
    print(error)
