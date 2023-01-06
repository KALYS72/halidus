'Абстракция - принцип ООП, в котором  создается класс пустышка, где задаются названия аттрибутов и методов, для того чтобы в дочерних классах не забыть их переопределить.'

from abc import ABC, abstractmethod, abstractproperty

class AbstractAnimal(ABC):
    @abstractproperty
    def legs(self):
        ...
    
    @abstractmethod
    def voice(self):
        ...

# obj = AbstractAnimal()
# TypeError: 'abstractproperty' object is not callable

class Dog(AbstractAnimal):
    def voice(self):
        print('bork-bork')

# obj = Dog()
# TypeError: Can't instantiate abstract class Dog with abstract method legs

class Cat(AbstractAnimal):
    legs = 4

# obj = Cat()
# obj.legs 
# TypeError: Can't instantiate abstract class Cat with abstract method voice


class Dog(AbstractAnimal):
    legs = 4

    def voice(self):
        print('bonk-bonk')

obj = Dog()
obj.voice()


