from django.urls import path
from .views import UserCreateView


urlpatterns = [
    path('cadastro/aluno/', UserCreateView.as_view(), name='cadastro_aluno'),
]
