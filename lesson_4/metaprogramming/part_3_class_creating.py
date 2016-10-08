# coding=utf-8

class A:
    pass
a = A()  # Вызывается __new__, затем __init__


class B:
    def __new__(cls, *args):
        obj = super(B, cls).__new__(cls, *args)
        print('Создался объект')
        return obj

    def __init__(self):
        print('Проинициализировался объект')


b = B()

