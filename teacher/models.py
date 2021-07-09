from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    teaching_hours=models.PositiveSmallIntegerField()
    units=models.CharField(max_length=10)
