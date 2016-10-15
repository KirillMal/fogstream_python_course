class WeakDescriptor:
    """Слабый дескриптор"""
    def __get__(self, instance, cls):
        print('вызывался дескриптор __get__')
        print(self)
        print(instance)
        print(cls)
        return 'WeakValue'

class A:
    desc = WeakDescriptor()

a = A()
a.desc # вызывает WeakDescriptor.__get__

a.desc = 11
a.desc



class StrongDesc:
    """
    Сильный дескриптор. Сильный - потому что
    """
    def __get__(self, instance, owner):
        return "StrongValue"
    def __set__(self, instance, value):
        pass

class B:
    desc = StrongDesc()
b = B()
b.desc  # StrongValue
b.desc = "NewValue"
b.desc  # StrongValue
