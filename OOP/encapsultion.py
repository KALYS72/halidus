'Инкапсуляция - принцип ООП, у которого есть 2 трактовки'
# 1.  сбор всех необходимых аттрибутов в единую  'капсулу' (class)
# 2.  сокрытие данных (ограничение доступа к аттрибуту)

'Виды доступа к аттрибутам'
# 1. public (публичные)
# 2. protected (защищенные) -  c одним андерскором _
# 3. private (приватные) - с двумя андерскорами в начале

class A:
    attr1 = 'public'
    _attr2 = 'protected'
    __attr3 = 'private'

print(A.attr1) # public
print(A._attr2) # protected
# print(A.__attr3) # AttributeError: type object 'A' has no attribute '__attr3'. Did you mean: '_A__attr3'?
print(A._A__attr3) # private
print(A.__dict__)

class B:
    x = 'hello'

    def __init__(self):
        self.y = 'world'

obj_b = B()
print(obj_b.__dict__) # {'y':'world'}
print(obj_b.x) # 'hello'

obj_b.hello = 'HELLO'
print(obj_b.hello) # HELLO

setattr(obj_b, 'VAL', 'NO') 
print(obj_b.__dict__) # {'y': 'world', 'hello': 'HELLO', 'VAL': 'NO'}



'-----------------------------------------------Getters/Setters-----------------------------------------------'
# функции, с помощью которых можно получать/изменять значение аттрибута

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else: raise Exception('Возраст не может быть меньше 0 и больше 120')

obj = Person('Nastya', 12)
print(obj.get_age()) # 12
obj.set_age(50)
print(obj.get_age()) # 50

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    'property делает из функции аттрибут'
    @property 
    def age(self):
        return self.__age

    'setter вызывается когда пишется obj.age = value'
    @age.setter
    def age(self, new_age):
        if new_age > 0 and new_age < 120:
            self.__age = new_age
        else: raise Exception('Возраст не может быть меньше 0 и больше 120')

    'deleter вызывается когда пишется del obj.age'
    @age.deleter
    def age(self):
        if self.__age < 100:
            raise Exception('No')
        del self.__age

obj = Person('Nastya', 12)
print(obj.age)
obj.age = 5 # AGE SETTER = 5
# obj.age = -1 # Exception


class Phone:
    def __init__(self, number):
        '+996 777 01-01-01'
        self.__number = number
   
    @property
    def number(self):
        'Функция для получения значения'
        return self.__number

    @number.setter
    def set_number(self, new_number):
        assert type(new_number) == str, 'Номер должен быть строкой'
        assert len(new_number) == 9, 'Номер должен состоять из 9 цифр'
        n = new_number
        self.__number = f'+996 {n[:3]} {n[3:5]}-{n[5:7]}-{n[7:]}'


obj = Phone('+996 777 01-01-01')
print(obj.number)
obj.set_number = '123456789'
print(obj._Phone__number)