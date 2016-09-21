from __future__ import unicode_literals
from ..mycourses.models import Courses, CourseDescriptions
from ..loginapp.models import Users
from django.db import models

# Create your models here.
class Classroom(models.Model):
    FK_course = models.ForeignKey(Courses, related_name='classroom_course')
    FK_student = models.ForeignKey(Users, related_name='classroom_student')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)