__author__ = 'fissalalsharef'

from django import forms
from Assignment3.models import *


class TeacherInfo(forms.Form):
    Teacher_Name = forms.CharField(max_length = 70)
    Teacher_LastName = forms.CharField(max_length = 70)
    Teacher_Email = forms.EmailField()
    Teacher_Phone = forms.IntegerField()
    Teacher_Office = forms.CharField(max_length = 500)


class StudentInfo(forms.Form):
    Student_Name = forms.CharField(max_length = 70)
    Student_LastName = forms.CharField(max_length = 70)
    Student_Email = forms.EmailField()

courses = [(course.C_Name,course.C_Name) for course in Courses.objects.all()]
students = [(student.Student_Name,student.Student_Name) for student in Student.objects.all()]
class EnrollForm(forms.Form):
    courses = forms.ChoiceField(courses, required=False,widget=forms.Select())
    students =forms.ChoiceField(students,required=False,widget=forms.Select())

class CoursesInfo(forms.Form):
    C_Name = forms.CharField(max_length = 70)
    C_Code = forms.CharField(max_length = 30)
    C_Classroom = forms.CharField(max_length = 30)
    C_Time = forms.TimeField()
    C_Teacher = forms.ModelChoiceField(queryset = Teacher.objects.all())