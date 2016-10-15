"""
Пользовательские атрибуты и методы
"""


class ClassA:
    var = 100500

    def func(self):
        return self.var


print(ClassA.__dict__)
# {'__module__': '__main__', 'var': 1,
# 'func': <function func at 0x7fc8473f2668>, '__doc__': None}

a = ClassA()
print(a.__dict__)
# {}
print(a.var)


# 100500

class B(ClassA):
    pass


B.__bases__
# (__main__.ClassA, )

"""
Поиск атрибутов объекта происходит следующим образом:
объект.атрибут

1. Поиск значения атрибут в таблице объект.__dict__ и во встроенных атрибутах
2. Поиск в объект.__class__ и во встроенных объект.__class__
3. Поиск в объект.__class__.__bases__
"""

ClassA.var is ClassA.__dict__['var']
# True
a.var is ClassA.__dict__['var']


# True

class ClassB:
    name = 'Борис'


a.__class__ = ClassB
a.var
# *** AttributeError: 'ClassB' object has no attribute 'var'

a.name  # Борис
