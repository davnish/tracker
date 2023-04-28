from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Teachers, Attendance
from datetime import date

authorized = None

def index(request):
    if request.method == 'POST' and request.POST.get('category') == "1":
        students = Student.objects.all()
        for student in students:
            if request.POST.get('fname') == student.name and request.POST.get('pwd') == student.roll_number:
                global authorized
                authorized = request.POST.get('fname')
                print(authorized)
                return redirect('students_mark')
    elif request.method == 'POST' and request.POST.get('category') == "0":
        teachers = Teachers.objects.all()
        for teacher in teachers:
            if request.POST.get('fname') == teacher.name and request.POST.get('pwd') == teacher.password:
                authorized = request.POST.get('fname')
                return redirect('teachers_view')
    else:
        students = Student.objects.all()
        return render(request, 'tracker/login.html')

def mark_attendance(request):
    global authorized
    authorized = Student.objects.filter(name = authorized).first()
    if request.method == 'POST':
        status = request.POST.get('Attendence', False)
        print(status)
        Attendance.objects.create(student=authorized, date=date.today(), status=status)
        return redirect('tracker-home')
    else:
        return render(request, 'tracker/students.html', {'student': authorized})

def view_attendance(request):
    # global authorized
    # authorized = Teachers.objects.filter(name = authorized).first()
    
    attendance_records = Attendance.objects.all()
    return render(request, 'tracker/teachers.html', {'attendance_records': attendance_records, 'teacher':authorized})
    



