from django.urls import path
from .views import StudentListView, StudentSubjectListView

urlpatterns = [
    path('', StudentListView.as_view(), name='student'),
    path('minhas_turmas/', StudentSubjectListView.as_view(),
         name='student_subjects'),
]
