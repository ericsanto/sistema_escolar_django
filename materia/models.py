from django.db import models
from aluno.models import Student


class Subject(models.Model):
    name = models.CharField('Nome: ',  max_length=255)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    first_grade = models.DecimalField(
        'Primeira Nota:', max_digits=4, decimal_places=2, default=None)
    second_grade = models.DecimalField(
        'Segunda Nota:',  max_digits=4, decimal_places=2, default=None)
