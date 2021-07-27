from django.shortcuts import render
# from .forms import StudentRegistrationForm
from student.models import Student
from .forms import StudentRegistrationForm

def register_student(request):
    form=StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})
# Create your views here.
