from django.db import models


class Subject(models.Model):
    name = models.CharField('Nome: ',  max_length=255)

    def __str__(self):
        return self.name


class Material(models.Model):
    title_material = models.CharField(max_length=255)
    file_material = models.FileField(upload_to='meterials/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title_material
