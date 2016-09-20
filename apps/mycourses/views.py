from django.shortcuts import render, redirect
from django.contrib import messages
from . import models

# Create your views here.
def index(request):
    context = {}
    courses = models.Courses.objects.all()
    context['courses'] = courses
    return render(request, 'mycourses/index.html', context)

def addcourse(request):
    context = {}
    if request.method == 'POST':
        c_name = request.POST['c_name']
        c_desc = request.POST['c_desc']
        if len(c_name) < 1 :
            messages.add_message(request, messages.ERROR , 'Course name is empty')
            return redirect('/')
        elif len(c_desc) < 1 :
            messages.add_message(request, messages.ERROR, 'Please add a description for the course.')
            return redirect('/')
        else:
            course = models.Courses.objects.create(name = c_name)
            course.save()
            courseFK = course.id
            coursedescription = models.CourseDescriptions.objects.create(FK_course_name = course, description = c_desc)
            coursedescription.save()
            return redirect('/')
    else: 
        return redirect('/')

def deletecourse(request, courseid):
    context = {}
    delcoursedesc = models.CourseDescriptions.objects.get(FK_course_name__id=courseid)
    delcourse = models.Courses.objects.get(id=courseid)
    context['delcoursedesc'] = delcoursedesc
    context['delcourse'] = delcourse
    context['courseid'] = courseid
    print courseid
    return render(request, 'mycourses/delete.html', context)

def confirmdelete(request, courseid):
    if request.method == 'POST':
        print courseid
        models.CourseDescriptions.objects.get(FK_course_name__id=courseid).delete()
        models.Courses.objects.get(id=courseid).delete()
        return redirect('/')
    else:
        return redirect('/')