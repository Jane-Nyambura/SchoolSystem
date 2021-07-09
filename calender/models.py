from django.db import models

# Create your models here.

class Calender(models.Model):
    type=models.CharField(max_length=10)
    course_name=models.CharField(max_length=10)
    price=models.PositiveSmallIntegerField()
    days=models.CharField(max_length=10)
    date=models.DateField()
    months=models.CharField(max_length=10)



