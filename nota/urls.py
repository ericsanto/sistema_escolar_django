from django.urls import path
from .views import GradeListView

urlpatterns = [
    path('minhas_notas/', GradeListView.as_view(), name='grade_list'),
]
