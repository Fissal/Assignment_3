from __future__ import unicode_literals
from django.db import models

class Teacher(models.Model):
    Teacher_Name = models.CharField(max_length = 70)
    Teacher_LastName = models.CharField(max_length = 70)
    Teacher_Email = models.EmailField()
    Teacher_Phone = models.IntegerField()
    Teacher_Office = models.CharField(max_length = 500)


class Student(models.Model):
    Student_Name = models.CharField(max_length = 70)
    Student_LastName = models.CharField(max_length = 70)
    Student_Email = models.EmailField()


class Courses(models.Model):
    C_Name = models.CharField(max_length = 70)
    C_Code = models.CharField(max_length = 30)
    C_Classroom = models.CharField(max_length = 30)
    C_Time = models.TimeField()
    C_Teacher = models.ForeignKey(Teacher)
    C_student = models.ManyToManyField(Student)



