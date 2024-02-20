from django.db import models
from materia.models import Subject


class Student(models.Model):
    name = models.CharField('Nome', max_length=255)
    subject = models.ManyToManyField(Subject)
