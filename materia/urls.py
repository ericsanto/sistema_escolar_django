from django.urls import path
from .views import SubjectDetailView, MaterialDetailView


urlpatterns = [
    path('detalhes_materia/<int:pk>/',
         SubjectDetailView.as_view(), name='detail_subject'),
    path('download_arquivo/<int:pk>/',
         MaterialDetailView.as_view(), name='download_file'),
]
