from django.urls import path
from .views import TeacherTemplateView

urlpatterns = [
    path('', TeacherTemplateView.as_view(), name='teacher')
]
