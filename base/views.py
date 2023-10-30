from django.shortcuts import render, redirect
import math
import smtplib
import random
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import authenticate, login, logout
from .models import Course, Teacher, Topic, Student, PurchaseAndEnrolment
from django.core.mail import send_mail
from django.conf import settings

login_status=False
random_str = ''
digits = [i for i in range(0, 10)]
for i in range(6):
    index = math.floor(random.random() * 10)
    random_str += str(digits[index])
student={}  


def student2FA(request,pk):
    student=Student.objects.get(name=pk)
    email=student.email
    

    q = request.POST.get('otp')
    if random_str==str(q):
        return redirect('studentmain',student.name)
        
    context={'student':student}
    return render(request,'base/student2fa.html',context)
    
 
def studentMainPage(request,pk):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
        course = Course.objects.filter(courseName__icontains=q)

    else:
        course = Course.objects.all()
        q = "All"
        
    student=Student.objects.get(name=pk)

    context = {'course': course, 'q': q,'student':student}
    return render(request,'base/student_main_page.html',context)

def studentRegister(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        address=request.POST['address']
        age=request.POST['age']
        gender=request.POST['gender']
        
        new_student=Student(name=name,email=email,password=password,phone=phone,address=address,age=age,gender=gender)
        new_student.save()
        
        return redirect('login')
    
    context={}
    return render(request,'base/student_register.html',context)
    
    
def loginPage(request):
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(email=email)
            if student.password == password:
                
                    
                fromaddr = '20d18@sdmit.in'  
                toaddrs  = email 
                msg = random_str

                username = '20d18@sdmit.in'  
                password = 'Charan@1234' # Here

                server = smtplib.SMTP('smtp.gmail.com', 587)  
                server.ehlo()
                server.starttls()
                server.login(username, password)  
                server.sendmail(fromaddr, toaddrs, msg)  
                server.quit()        
                return redirect('student2fa',student.name)

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

def studentCourses(request, pk):
    course = Course.objects.get(id=pk)
    teacher_name = course.teacher_id
    teacher = Teacher.objects.get(name=teacher_name)
    context1 = {'course': course}

    context2 = {'teacher': teacher}
    context3 = {'student': student}
    context = {**context1, **context2,**context3}

    return render(request, 'base/studentcourses.html', context)