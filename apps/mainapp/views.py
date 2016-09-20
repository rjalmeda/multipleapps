from django.shortcuts import render,redirect
from django.contrib import messages
from ..loginapp.models import Users
from ..mycourses.models import Courses, CourseDescriptions

# Create your views here.
def index(request):
    return render(request, 'index.html')