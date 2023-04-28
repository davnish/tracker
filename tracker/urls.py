from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='tracker-home'),
    path('students-mark', views.mark_attendance, name='students_mark'),
    path('teacher-view', views.view_attendance, name='teachers_view')
]
