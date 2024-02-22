from django.contrib import admin
from .models import Grade


class GradeAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject',
                    'first_grade', 'second_grade', 'average']


admin.site.register(Grade, GradeAdmin)
