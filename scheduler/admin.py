# scheduler/admin.py

from django.contrib import admin
from .models import Course, StudySession, Task

admin.site.register(Course)
admin.site.register(StudySession)
admin.site.register(Task)
