from django.shortcuts import render,redirect
from django.contrib import messages
from ..loginapp.models import Users
from ..mycourses.models import Courses, CourseDescriptions
from .models import Classroom

# Create your views here.
def index(request):
    context = {}
    courses = Courses.objects.all()
    context['courses'] = courses
    return render(request, 'mainapp/index.html', context)

def register(request, courseid):
    studentid = request.session['userid']
    targetStudent = Users.userManager.get(id=studentid)
    targetCourse = Courses.objects.get(id=courseid)
    studentpresent = 0
    try: 
        studentpresent = Classroom.objects.filter(FK_course=targetCourse).filter(FK_student=targetStudent).count()
        print studentpresent
    except:
        studentpresent = 0
    if studentpresent == 0:
        Classroom.objects.create(FK_course = targetCourse, FK_student = targetStudent).save()
        print 'Student Registered'
    else:
        print 'Student Already Registered'
    return redirect('/')
def reset(request):
    request.session.clear()
    request.session.flush()
    return redirect('/')
