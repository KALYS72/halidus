'существует 3 вида методов'
# instance methods - обычные методы, который принимают первый аргументом self (ссылка на объект). нужны они для работы с атрибутами объекта
 
# class methods - принимают первым аргументом ссылку на cls(класс). Нужны они для создания объектов или изменения атрибутов класса. 
class A:
    def instance_method(self):
        print('obj method')
        print('first arg:', self)
obj = A()
obj.instance_method() # если вызываем у объекта, то self передаетя автоматически
A.instance_method(obj) # если вызываем у класса, то в self нужно передать объект от этого класса

class B:
    @classmethod
    def class_method(cls):
        print('class method')
        print('first arg', cls)

obj_b = B()
obj_b.class_method()
B.class_method() # не важно будем ли вызывать класс метод у класса или у объекта, в певый аргумент придет ссылка на класс

class C:
    counter = 0
    def __init__(self):
        self._inc_counter()

    def __del__(self):
      self._dec_counter()
      self.counter -= 1
        

    @classmethod
    def _inc_counter(cls):
        cls.counter +=1

    @classmethod
    def _dec_counter(cls):
        cls.counter -=1

obj1 = C()
obj2 = C()
obj3 = C()
print(C.counter)
print(obj1.counter)
print(obj2.counter)
print(obj3.counter)


class Pizza:
  def __init__(self,radius, *ingridients):
    self.radius = radius
    self.ingridients = ingridients
  def cook(self):
    print(f'готовится пицца с размером {self.radius * 2} см')
    print(f'ингридиенты: {self.ingridients}')
  
pizza1 = Pizza(15, 'Пепперони', 'Моцарелла', 'Ананас')
pizza2 = Pizza(15, 'Моцарелла', 'еще сыр', 'Голландский', 'Дор блю')
pizzas = [pizza1, pizza2]
for i in pizzas:
  i.cook()




# static methods - методы, которые принимают первым аргументом cls(ссылка на класс). Нужны для создания объектов или изменения атрибутов класса. Для создания метода