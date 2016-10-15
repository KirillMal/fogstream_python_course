"""
Использование метаклассов
"""
from django.db import models

# в models.Model переопределены метаклассы
class Person(models.Model):
    name = models.CharField('Имя', max_length=50)
    age = models.IntegerField()

super_man = Person(name='Андрей', age=30)

print(super_man.age)
# 30

