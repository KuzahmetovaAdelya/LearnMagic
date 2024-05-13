from django.db import models

# Create your models here.
class Persons(models.Model):
    name = models.CharField('Имя', max_length=50, default='')
    password = models.CharField('Пароль', max_length=20, default='')
    role = models.CharField("Роль", max_length=10, default='0')

    def __str__(self):
        return self.name
    