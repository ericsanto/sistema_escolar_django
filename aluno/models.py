from django.db import models
from disciplina.models import Subjects


class Student(models.Model):
    name = models.CharField('Nome', max_length=255)
    subjects = models.ManyToManyField(Subjects)
