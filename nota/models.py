from django.db import models
from aluno.models import Student
from materia.models import Subject


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    first_grade = models.DecimalField(
        'Primeira Nota', max_digits=4, decimal_places=2)
    second_grade = models.DecimalField(
        'Segunda Nota', max_digits=4, decimal_places=2)
