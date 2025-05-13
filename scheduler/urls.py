# scheduler/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

class LogoutGetView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='courses'),
    path('sessions/', views.session_list, name='sessions'),
    path('tasks/', views.tasks_list, name='tasks'),
    path('login/', auth_views.LoginView.as_view(template_name='scheduler/login.html'), name='login'),
    path('logout/', LogoutGetView.as_view(), name='logout'),
    path('register/', views.register, name='register'),

    # Forgot Password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='scheduler/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='scheduler/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='scheduler/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='scheduler/password_reset_complete.html'), name='password_reset_complete'),


    # Add Course
    path('courses/', views.course_list, name='courses'),
    path('courses/add/', views.add_course, name='add_course'),

    path('study_sessions/', views.study_sessions, name='sessions'),
    path('study_sessions/add/', views.add_session, name='add_session'),
    path('study_sessions/edit/<int:pk>/', views.edit_session, name='edit_session'),
    path('study_sessions/delete/<int:pk>/', views.delete_session, name='delete_session'),

    path('tasks', views.task_list, name='tasks'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
]
