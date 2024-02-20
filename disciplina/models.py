from django.db import models


class Subjects(models.Model):
    name = models.CharField('Disciplina:', max_length=255)
    grade_one = models.DecimalField(max_digits=5, decimal_places=2)
    grade_two = models.DecimalField(max_digits=5, decimal_places=2)
    frequency = models.BooleanField('Frequencia:', default=False)
