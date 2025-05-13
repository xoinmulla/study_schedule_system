# scheduler/models.py

from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    credits = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class StudySession(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.name} on {self.session_date}"


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['due_date']
