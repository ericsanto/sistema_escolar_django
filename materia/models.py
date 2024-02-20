from django.db import models


class Subject(models.Model):
    name = models.CharField('Nome: ',  max_length=255)
    first_grade = models.DecimalField(
        'Primeira Nota:', max_digits=4, decimal_places=2, default=None)
    second_grade = models.DecimalField(
        'Segunda Nota:',  max_digits=4, decimal_places=2, default=None)
