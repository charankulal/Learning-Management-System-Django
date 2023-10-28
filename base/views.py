from django.shortcuts import render



def home(request):
    context={'courses':course_dict}
    return render(request,'base/home.html',context)

def courses(request,pk):
    courses=
    context1={'courses':courses}
    return render(request,'base/courses.html',context1)
