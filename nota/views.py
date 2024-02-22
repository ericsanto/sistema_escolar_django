from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Grade
from aluno.models import Student
from materia.models import Subject


class GradeListView(ListView):
    model = Grade
    template_name = 'grade.html'
    context_object_name = 'grades'

    def get_queryset(self):
        grade_student = Grade.objects.filter(
            student__registration=self.request.user)
        return grade_student

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['student'] = Student.objects.filter(
            registration=self.request.user)

        context['student_subjects'] = Subject.objects.filter(
            student__registration=self.request.user)

        context['subject'] = Subject.objects.filter(
            student__registration=self.request.user)
        return context
