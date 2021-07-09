from django.db import models

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=10)
    duration=models.PositiveSmallIntegerField()
    tittle=models.CharField(max_length=10)
    units=models.CharField(max_length=10)
    stack=models.CharField(max_length=10)


