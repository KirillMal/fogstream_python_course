print(object)
# class <object>

print(type)
# <class 'type'>

print(type(object))
# <class 'type'>

print(type(type))
# <class 'type'>

print(object.__class__)
# <class 'type'>

print(object.__bases__)
# ()

print(type.__class__)
# <class 'type'>

print(type.__bases__)
# (<class 'object'>,)

# Python 2.x
class Old:
    pass
old = Old()
type(old)  # type <instance>

class New(object):
    pass
new = New()
type(new)  # type <New>

"""
Объекты-типы - представление абстрактных типов данных
тип == класс

Типом любого объекта-типа является type
"""



type(list)
# <class 'type'>

type([1, 2, 3])
# <class 'list'>

type(tuple)
# <class 'type'>

type((1, 2, 3))
# <class 'tuple'>