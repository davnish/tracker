from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    # other fields like email, phone, etc.

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student.name} ({self.date}): {"Present" if self.status else "Absent"}'
    
class Teachers(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
# Create your models here.
