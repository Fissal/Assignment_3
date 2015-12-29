__author__ = 'fissalalsharef'

from Assignment3.forms import *
from Assignment3.models import *
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext


def addteacher(request):
    if request.method == 'POST':
        form = TeacherInfo(request.POST)
        if form.is_valid():
            a = Teacher(Teacher_Name = form.cleaned_data["Teacher_Name"],
                        Teacher_LastName = form.cleaned_data["Teacher_LastName"],
                        Teacher_Email = form.cleaned_data["Teacher_Email"],
                        Teacher_Phone = form.cleaned_data["Teacher_Phone"],
                        Teacher_Office = form.cleaned_data["Teacher_Office"])
            a.save()
            return HttpResponseRedirect('/allteacher/')

    else:
        form = TeacherInfo()

    return render_to_response('addteacher.html',{'form':form},RequestContext(request))


def allteacher(request):
    return render_to_response('allteacher.html', {'Teacherlist': Teacher.objects.all()})


def addstudent(request):
    if request.method == 'POST':
        form = StudentInfo(request.POST)
        if form.is_valid():
            a = Student(Student_Name = form.cleaned_data["Student_Name"],
                        Student_LastName = form.cleaned_data["Student_LastName"],
                        Student_Email = form.cleaned_data["Student_Email"])
            a.save()
            return HttpResponseRedirect('/allstudent/')

    else:
        form = StudentInfo()

    return render_to_response('addstudent.html',{'form':form},RequestContext(request))


def allstudent(request):
    return render_to_response('allstudent.html', {'Studentlist': Student.objects.all()})

def addCourses(request):
    if request.method == 'POST':
        form = CoursesInfo(request.POST)
        if form.is_valid():
            a = Courses(C_Name = form.cleaned_data["C_Name"],
                        C_Code = form.cleaned_data["C_Code"],
                        C_Classroom = form.cleaned_data["C_Classroom"],
                        C_Time = form.cleaned_data["C_Time"],
                        C_Teacher = form.cleaned_data["C_Teacher"])
            a.save()
            return HttpResponseRedirect('/allCourses/')

    else:
        form = CoursesInfo()

    return render_to_response('addCourses.html',{'form':form},RequestContext(request))


def allCourses(request):
    return render_to_response('allCourses.html', {'Courselist': Courses.objects.all()})

def chooseCourse(request):
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            studentname = Student.objects.get(Student_Name = form.cleaned_data["students"])
            coursename = Courses.objects.get(C_Name = form.cleaned_data["courses"])

            coursename.C_student.add(studentname)
            return HttpResponseRedirect('/Listed/'+form.cleaned_data["courses"])

    form = EnrollForm()
    return render_to_response('chooseCourse.html',{'form':form},RequestContext(request))


def chosenCourse(request,a):
    c = Courses.objects.get(C_Name = a)
    return render_to_response('showCourses.html', {'courseStudetList': c.C_student.all()})


