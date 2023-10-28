from django.shortcuts import render

course_dict=[
    {
        'id':1,
        'name':'Lets learn python'
        
    },
    {
        'id':2,
        'name':'Lets learn Java'
        
    },
    {
        'id':3,
        'name':'Lets learn c'
        
    },
    {
        'id':4,
        'name':'Lets learn c++'
        
    },
    
]

def home(request):
    context={'courses':course_dict}
    return render(request,'base/home.html',context)

def courses(request,pk):
    courses=None
    for course in course_dict:
        if course['id']==int(pk):
            courses=course
            break
    context={'courses':courses}
    return render(request,'base/courses.html',context)
