'Ассоциация - принцип ООП, в котором 2 класса связаны с друг другом'
# агрегация - слабая связь
# композиция - сильная связь

class Battery:
    _power = 100

    def charge(self):
        if self._power != 100:
            self._power = 100
            return f'Заряд: {self._power}'
        return 'Заряд полон'

class Iphone:
    def __init__(self, color) -> None:
        self.color = color
        self.battery = Battery()
        # когда мы создаем обьект от другого обьекта внутри класса - это композици
        
class Nokia:
    def __init__(self, battery:Battery, color:str='черный'):
        self.battery = battery
        self.color = color

iphone = Iphone('Золотой')
del iphone
# при удалении айфона вместе с ним удаляется батарея
'Композиция (сильная связь)'

battery = Battery()
nokia1 = Nokia(battery, 'серый')
del nokia1

nokia2 = Nokia(battery, 'красный')
del nokia2 
# при удалении nokia2, батарейка остается

iphone = Iphone('Серый')
b = Battery()
nokia = Nokia(b)

print(iphone.battery._power)
nokia.battery._power = 50
print(nokia.battery._power) # 50
nokia.battery.charge()
print(nokia.battery._power) # 100

