# scheduler/views.py

from django.shortcuts import render
from .models import Course, StudySession, Task

def home(request):
    return render(request, 'scheduler/index.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'scheduler/courses.html', {'courses': courses})

def session_list(request):
    sessions = StudySession.objects.all()
    return render(request, 'scheduler/sessions.html', {'sessions': sessions})

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, 'scheduler/tasks.html', {'tasks': tasks})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'scheduler/register.html', {'form': form})


# views.py
from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'scheduler/courses.html', {'courses': courses})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')  # Redirect back to the courses list after saving
    else:
        form = CourseForm()

    return render(request, 'scheduler/add_course.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from .models import StudySession, Course
from .forms import StudySessionForm

# Read: Display Study Sessions
def study_sessions(request):
    sessions = StudySession.objects.all()
    return render(request, 'scheduler/sessions.html', {'sessions': sessions})

# Create: Add a new Study Session
def add_session(request):
    if request.method == 'POST':
        form = StudySessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sessions')
    else:
        form = StudySessionForm()
    return render(request, 'scheduler/add_session.html', {'form': form})

# Update: Edit an existing Study Session
def edit_session(request, pk):
    session = get_object_or_404(StudySession, pk=pk)
    if request.method == 'POST':
        form = StudySessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('sessions')
    else:
        form = StudySessionForm(instance=session)
    return render(request, 'scheduler/edit_session.html', {'form': form})

# Delete: Delete a Study Session
def delete_session(request, pk):
    session = get_object_or_404(StudySession, pk=pk)
    session.delete()
    messages.success(request, 'session deleted successfully!')
    return redirect('sessions')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib import messages

# Display all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'scheduler/tasks.html', {'tasks': tasks})

# Create a new task
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task added successfully!')
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'scheduler/add_task.html', {'form': form})

# Update an existing task
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'scheduler/edit_task.html', {'form': form, 'task': task})

# Delete a task
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('tasks')
