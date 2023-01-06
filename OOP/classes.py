'=================================OOP================================='
# OOP - object-orientated programing
# ООП - обьктно ореинтированное программирование



class Person:
    # переменные внутри класса (обьекты) - аттрибуты
    arms= 2
    legs= 2

    # функции внутри класса (обьекты) - методы
    def __init__(self, name, age):
        # init - метод который будет добавлять в обьект те атрибуты в обьект, которые отличаются у разных обьектов
        # self - ссылка на обьект, который только что создался
        self.name = name
        self.age = age
        
    def walk(self):
        print(f'{self.name} ходит')

    def happy_birhday(self):
        print(f'{self.name}, Happy Birthday!')
        self.age += 1
        print('Подарок')

    

# obj1 = Person()
# obj2 = Person()
obj1 = Person('Nastya', 12)
obj2 = Person('Kalys', 16)
print(obj1.name)
print(obj2.name)
obj1.walk() # Nastya ходит
obj2.walk() # Kalys ходит
# Person.name()  AttributeError: type object 'Person' has no attribute 'name'   

obj1.hello = 'Hello'
print(obj1.hello) # Hello
# print(obj2.hello) # AttributeError: 'Person' object has no attribute 'hello'

print('AGE:', obj1.age)
obj1.happy_birhday()
obj1.happy_birhday()
obj1.happy_birhday()
print(obj1.age)
# AGE: 12
# Nastya, Happy Birthday!
# Nastya, Happy Birthday!
# Nastya, Happy Birthday!
# 15


'------------------------------------------------------------Обьекты класса-------------------------------------------------------'
# обьект, экземпляр, instance класса - обьект, созданный по шаблону класса (он перенимает все артибуты и методы класса)

'-------------------------------------------------------------Атрибуты-------------------------------------------------------------'
# Атрибуты - переменные
# Методы - функции

class A:
    var1 = 'переменная класса'

    def __init__(self):
        self.var2 = 'переменная обьекта'

    def __str__(self):
        return 'обьект от класса А'

# print(dir(A))
# ['___init__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1']
# нет var2

obj = A()
print(dir(obj))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var1', 'var2']

print(obj) # обьект от класса А

print(obj.__class__) # <class '__main__.A'>

'Класс не имеет доступа к обьектам'
'с помощью Аттрибута __class__ мы можем обратится к классу от которого создан обьект'


print(type.__class__) # <class 'type'>
print(A.__class__) # <class 'type'>

class Calc:
    def add(self, a, b):
        '+'
        return a + b
    
    def sqrt(self, num, ndigits=2):
        'Квадратный корень'
        import math 
        sqrt_num = math.sqrt(num)
        return round(sqrt_num, ndigits)
    
    def percent(self, total, _percent):
        return (total * _percent) / 100

    def super_func(self, string):
        'функция, которая выполняет выичсления в строке'
        return eval(string)

calc = Calc()
print(calc.add(4,5)) # 9
print(calc.sqrt(2354, 1))  # 48.5
print(calc.percent(60, 10)) # 6.0
print(calc.percent(258, 567)) # 1462.86
print(calc.super_func('256 / 100 * 35')) # 89,6




class B:
    var = 4
    def __init__(self, a):
        self.a = a


obj = B(5)
B.__init__(obj, 5)