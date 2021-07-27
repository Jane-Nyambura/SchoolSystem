from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=10)
    last_names=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    Id_number=models.CharField(max_length=10)
    nationality=models.CharField(max_length=10)
    passport_photo=models.FileField()
    phone_number=models.PositiveIntegerField()
    medical_report=models.FileField()
    room_number=models.PositiveSmallIntegerField()
    class_name=models.CharField(max_length=10)
    big_sister=models.CharField(max_length=10)
    mentor_name=models.CharField(max_length=10)
    email_address=models.EmailField()
    # Asset_number=models.ForeignKey()
    GENDER_CHOICES=(
        (u'M','Male'),
        (u'F','Female'),
        (u'O','Others')
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    County=models.CharField(max_length=10)
    # Guardian_name=models.ForeignKey()
    # Emergency_Contact=models.ForeignKey()










