from django.db import models
from materia.models import Subject
import random
from datetime import date


class Teacher(models.Model):
    name = models.CharField('Nome', max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    registre_job = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.registre_job:
            year = str(date.today().year)
            numbers = list()
            for a in range(11):
                numbers.append(str(random.randint(0, 9)))

            values = [year] + numbers
            self.registre_job = ''.join(values)
        super().save(*args, **kwargs)
