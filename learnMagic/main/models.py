from django.db import models

# Create your models here.
class Persons(models.Model):
    name = models.CharField('Имя', max_length=50, default='')
    password = models.CharField('Пароль', max_length=20, default='')
    role = models.CharField("Роль", max_length=10, default='0')

    def __str__(self):
        return self.name
    

class Answer(models.Model):
    gameName = models.CharField('Название', max_length=50, default='')
    answer = models.CharField('Ответ', max_length=100, default='1')
    
    def __str__(self):
        return self.gameName