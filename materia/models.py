from django.db import models


class Subject(models.Model):
    name = models.CharField('Nome: ',  max_length=255)
