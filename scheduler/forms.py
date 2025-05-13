# forms.py
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'credits','description']  # Add any other fields that your course model has

from django import forms
from .models import StudySession

class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['course', 'session_date', 'start_time', 'end_time']
        widgets = {
            'session_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }


from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']
