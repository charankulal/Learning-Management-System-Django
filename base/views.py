from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate, login, logout
from .models import Course, Teacher, Topic, Student, PurchaseAndEnrolment

login_cnd = False

def studentMainPage(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
        course = Course.objects.filter(courseName__icontains=q)

    else:
        course = Course.objects.all()
        q = "All"

    context = {'course': course, 'q': q}
    return render(request,'base/student_main_page.html',context)


def loginPage(request):
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
            # student = Student.objects.get(email=email)
            # if student.password == password:
            #     login_cnd = True
                # context1={'student':student}
                # return render(request,'base/student_main_page',context)
                return redirect('studentmain')

        except:
            messages.error(request, "User Doesn't exist")

    return render(request, 'base/register_login.html', context)


def home(request):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
        course = Course.objects.filter(courseName__icontains=q)

    else:
        course = Course.objects.all()
        q = "All"

    context = {'course': course, 'q': q}
    return render(request, 'base/home.html', context)


def courses(request, pk):
    course = Course.objects.get(id=pk)
    teacher_name = course.teacher_id
    teacher = Teacher.objects.get(name=teacher_name)
    context1 = {'course': course}

    context2 = {'teacher': teacher}
    context = {**context1, **context2}

    return render(request, 'base/courses.html', context)
