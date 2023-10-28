from django.shortcuts import render
from .models import Course,Teacher,Topic,Student,PurchaseAndEnrolment



def home(request):
    course=Course.objects.all()
    context={'course':course}
    return render(request,'base/home.html',context)

def courses(request,pk):
    course=Course.objects.get(id=pk)
    teacher_name=course.teacher_id
    teacher=Teacher.objects.get(name=teacher_name)
    context1={'course':course}
    
    context2={'teacher':teacher}
   
    return render(request,'base/courses.html',context1,context2)
