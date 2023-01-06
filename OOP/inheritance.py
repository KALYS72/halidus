'Наследование - принцип ООП, в котором мы можем унаследовать, переопределить или использовать в дочернем классе все аттрибуты и метода родительского класса'

class A:
    def method(self):
        print('Метод в классе А')

obj = A()
obj.method()

class B(A):
    '''
    Унаследовали все методы и аттрибуты у класса А
    '''
obj1 = B()
obj1.method() # метод в классе А


class C(A):
    '''
    Унаследовали все методы и аттрибуты у класса А и переопределили метод method
    '''

    def method(self):
        print('Метод в классе С')
obj_c = C()
obj_c.method() # Метод в классе С
obj.method() # Метод в классе А

class A():
    x = 'x in A'
    y = 'y in A'

class B(A):
    x = 'x in B'

print(A.x) # x in A
print(A.y) # y in A
print(B.x) # x in B
print(B.y) # y in A

'mro (method resolution order) - порядок действия аттрибутов'
print(B.mro()) #  [<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

print(dir(object))
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

class A:
    def my_range(self, n):
        return list(range(n+1))

print(A().my_range(5)) # [0, 1, 2, 3, 4, 5]

class B(A):
    def my_range(self):
        # return A.my_range(self, 10)
        'через super мы обращаемся к родительскому классу'
        return super().my_range(10)

print(B().my_range()) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


'----------------------------------------------Виды наследований----------------------------------------------'
# одиночное наследование (когда мы наследуем в дочернем классе от 1 класса)
# множественное наследование (когда мы наследуем в дочернем классе от нескольких классов)
# многоуровневое наследование (когда мы наследуемся от класса н которого есть родитель)
# иерархическое наследование (когда от одного родителя много дочерних классов)
# гибридное наследование (когда используются несколько видов наследования)

'--------------------------------------------Множества наследования--------------------------------------------'
class A:
    a = 'a'

class B:
    b = 'b'

class C(A,B):
    '''
    Наследовали все атрибуты у классов А и В
    '''
    c = 'c'

print(C().a) # a
print(C().b) # b
print(C().c) # c

class A:
    def method(self):
        print('Метод в классе А')

class B:
    def method(self):
        print('Метод в классе В')

class C(A,B):
    ...

print(C().method()) # Метод в классе А
print(C().method()) # Метод в классе А
print(C.mro()) # [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

'----------------------------------Проблемы множественного наследования----------------------------------'
# проблема ромба (решенная с помощью mro)

class A:
    def __str__(self):
        print('A')

class B:
    def __str__(self):
        print('B')

class C:
    def __str__(self):
        print('C')

A().__str__() # A
B().__str__() # B
C().__str__() # C

# проблема перекрестного наследования (не решенная)

class A:
    ...

class B:
    ...

class E(A,B):
    ...

class D(B,A):
    ...

class F(E,D):
    ...