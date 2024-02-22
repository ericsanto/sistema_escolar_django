from django.db import models
from aluno.models import Student
from materia.models import Subject


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    first_grade = models.DecimalField(
        'Primeira Nota', max_digits=4, decimal_places=2, blank=True, null=True)
    second_grade = models.DecimalField(
        'Segunda Nota', max_digits=4, decimal_places=2, blank=True, null=True)
    average = models.DecimalField(
        'Média', max_digits=4, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.subject.name

    def save(self, *args, **kwargs):

        if self.first_grade is None:
            self.first_grade = 0

        if self.second_grade is None:
            self.second_grade = 0

        if self.first_grade and self.second_grade:
            self.average = (self.first_grade + self.second_grade) / 2
        elif self.first_grade:
            self.average = self.first_grade / 2
        else:
            self.average = 0
        super().save(*args, **kwargs)
