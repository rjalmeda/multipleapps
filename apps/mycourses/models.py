from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class CourseDescriptions(models.Model):
    FK_course_name = models.ForeignKey(Courses, related_name='course_name')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
