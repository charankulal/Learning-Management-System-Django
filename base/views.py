from django.shortcuts import render
from .models import Course,Teacher,Topic,Student,PurchaseAndEnrolment



def home(request):
    course=Course.objects.all()
    context={'course':course}
    return render(request,'base/home.html',context)

def courses(request,pk):
    course=Course.objects.get(id=pk)
    context1={'course':course}
    return render(request,'base/courses.html',context1)
