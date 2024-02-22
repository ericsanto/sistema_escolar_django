from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from .models import Student
from nota.models import Grade
from materia.models import Subject


# class StudentTemplateView(TemplateView):
#    template_name = 'student.html'

class StudentListView(ListView):
    model = Student
    template_name = 'home_student.html'
    context_object_name = 'students'

    def get_queryset(self) -> QuerySet[Any]:
        student = Student.objects.filter(
            registration=self.request.user)
        return student

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['grades'] = Grade.objects.filter(
            student__registration=self.request.user)
        return context


class StudentSubjectListView(ListView):
    model = Student
    template_name = 'list_subject.html'
    context_object_name = 'subjects'

    def get_queryset(self) -> QuerySet[Any]:
        subject = Subject.objects.filter(
            student__registration=self.request.user)
        return subject
