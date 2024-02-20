from django.db import models
from aluno.models import Student
from materia.models import Subject


class Grade(models.Model):
    student = models.ForeignKey('Estudante', Student, on_delete=models.PROTECT)
    subject = models.ForeignKey('Disciplina', Subject, on_delete=models.PROTECT)
