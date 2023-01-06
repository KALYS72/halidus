'Магические методы (dunder - double underscore) - методы, у которых 2 нижних подчеркивания в начале и 2 в конце, магиsя в том, что мы не вызываем их напрямую, а они вызываются определенными операторами или функциями'

# __new__, __init__ - вызваются, когда создаем обьект
int(5)

# __add__
'5' + '5'
'5'.__add__('5')

# __str__
a = 5

str(a)
a.__str__()

print(a)

# __hash__
hash('aaa')
'aaa'.__hash__()

# __eq__
a == b
a.__eq__(b)

# __gl__ >
# __le__ <=
# __ge__ >=

# __getattribute__
string = 'hello'
string.lower
string.__getattribute__('lower')

getattr(string, 'dsgsdgwsg', None)
string.__getattribute__('dsgsdgwsg')

# getattr - функция, которая вызывает __getattribute__. если такого нет и был передан default ошибку не вызывает



# __setattr__
a = 'hello'

a.new_attr = 'NEW-ATTRIBUTE'
a.__setattr__(new_attr, value)
