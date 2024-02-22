from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Subject, Material
from sendfile import sendfile


class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subject_detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['materials'] = Material.objects.filter(
            subject__id=self.kwargs['pk'])
        return context


class MaterialDetailView(DetailView):
    model = Material
    template_name = 'download.html'

    def get_queryset(self) -> QuerySet[Any]:
        material = Material.objects.get(pk=self.kwargs['pk'])
        print(material)
        response = sendfile(
            self.request, material.file_material.path, attachment=True)
        return response
