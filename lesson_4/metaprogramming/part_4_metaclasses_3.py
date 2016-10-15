class Singleton(type):
    """
    Метакласс, запрещающий создавать новые инстансы класса
    """
    instance = None
    
    def __new__(cls, *args, **kwargs):
        print('Singleton __new__')
        return super(Singleton, cls).__new__(cls, *args, **kwargs)
        
    def __init__(self, *args, **kwargs):
        print('Singleton __init__')
        return super(Singleton, self).__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('Singleton __call__')
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        else:
            raise Exception('Нельзя больше создавать объектов этого класса!!!')
        return cls.instance

class A:
    pass
type ('A', (), {})

class ASingleton(metaclass=Singleton):
    var = 'var'

Singleton('ASingleton', (), {'var': 'var'})


a = ASingleton()
b = ASingleton()



class Final(type):
    """
    Метакласс, запрещающий создавать наследников класса
    """
    def __init__(cls, name, bases, namespace):
        super(Final, cls).__init__(name, bases, namespace)
        for klass in bases:
            if isinstance(klass, Final):
                raise TypeError(str(klass.__name__) + " is Final class")



class A:
    pass

class B(A, metaclass=Final):
    pass

class C(B):
    pass


