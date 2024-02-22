from django.db.models.signals import post_save
from django.dispatch import receiver
from materia.models import Subject
from aluno.models import Student
from nota.models import Grade


@receiver(post_save, sender=Subject)
def create_grade(sender, instance, created, **kwargs):
    if created:
        students = Student.objects.all()
        for student in students:
            Grade.objects.create(
                student=student,
                subject=instance,
                first_grade=0,
                second_grade=0,
                average=0,
            )
