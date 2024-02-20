from django.db import models


class Student(models.Model):
    name = models.CharField('Nome', max_length=255)
