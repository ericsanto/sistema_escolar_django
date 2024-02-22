from django.shortcuts import render
from django.views.generic import TemplateView


class TeacherTemplateView(TemplateView):
    template_name = 'teacher.html'
