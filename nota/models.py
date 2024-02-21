from django.db import models
from aluno.models import Student
from materia.models import Subject
from django.db.models import Avg


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    first_grade = models.DecimalField(
        'Primeira Nota', max_digits=4, decimal_places=2)
    second_grade = models.DecimalField(
        'Segunda Nota', max_digits=4, decimal_places=2)
    average = models.DecimalField(
        'Média', max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.student.name

    def save(self, *args, **kwargs):
        if self.first_grade and self.second_grade:
            self.average = (self.first_grade + self.second_grade) / 2
        super().save(*args, **kwargs)
