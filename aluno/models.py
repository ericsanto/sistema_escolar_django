from django.db import models
import re
import random
from datetime import date
from materia.models import Subject


class Student(models.Model):
    name = models.CharField('Nome', max_length=255)
    number_rg = models.CharField(
        'Número do RG', max_length=9, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=11)
    address = models.CharField('Endereço', max_length=255)
    name_father = models.CharField(
        'Nome do Pai', max_length=255, blank=True, null=True)
    name_mather = models.CharField(
        'Nome da Mãe', max_length=255, blank=True, null=True)
    registration = models.CharField(
        'Matrícula', max_length=15, blank=True, null=True)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.registration:
            year = str(date.today().year)
            num = list()
            for i in range(6):
                num.append(str(random.randint(0, 9)))
            values = [year] + num
            self.registration = ''.join(values)
        super().save(*args, **kwargs)
