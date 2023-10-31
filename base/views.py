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
student1={}  
context3={}


def student2FA(request,pk):
    student1=Student.objects.get(name=pk)
    email=student1.email
    

    q = request.POST.get('otp')
    if random_str==str(q):
        return redirect('studentmain',student1.name)
        
    context={'student':student1}
    return render(request,'base/student2fa.html',context)
    
 
def studentMainPage(request,pk):
    if request.GET.get('q') != None:
        q = request.GET.get('q')
        course = Course.objects.filter(courseName__icontains=q)

    else:
        course = Course.objects.all()
        q = "All"
        
    student=Student.objects.get(name=pk)

    context3 = {'course': course, 'q': q,'student':student}
    return render(request,'base/student_main_page.html',context3)

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

def studentCourses(request,sk, pk):
    course = Course.objects.get(id=pk)
    teacher_name = course.teacher_id
    teacher = Teacher.objects.get(name=teacher_name)
    student=Student.objects.get(name=sk)
    context1 = {'course': course}

    context2 = {'teacher': teacher,'student':student1}
    context3 = {'student': student}
    context = {**context1, **context2,**context3}

    return render(request, 'base/studentcourses.html', context)

def studentMyCourses(request,pk):
    student=Student.objects.get(name=pk)
    purchasedCourses=PurchaseAndEnrolment.objects.filter(student_id=student.id)
    context={'student':student,'purchasedCourses':purchasedCourses}

    return render(request, 'base/studentmycourses.html', context)

def studentMyCourseStudy(request,sk,pk):
    course = Course.objects.get(id=pk)
    topics=Topic.objects.filter(course_id=pk)
    teacher_name = course.teacher_id
    teacher = Teacher.objects.get(name=teacher_name)
    student=Student.objects.get(name=sk)
    purchasedCourses=PurchaseAndEnrolment.objects.filter(student_id=student.id)
    
    context1 = {'course': course}

    context2 = {'teacher': teacher,'student':student1}
    context3 = {'student': student,'purchasedCourses':purchasedCourses,'topics':topics}
    context = {**context1, **context2,**context3}

    return render(request, 'base/studentmycoursestudy.html', context)

def studentBuyCourse(request,sk, pk):
    course = Course.objects.get(courseName=pk)
    teacher_name = course.teacher_id
    teacher = Teacher.objects.get(name=teacher_name)
    student=Student.objects.get(name=sk)
    context1 = {'course': course}

    context2 = {'teacher': teacher,'student':student1}
    
    try:
        ispurchased=PurchaseAndEnrolment.objects.get(course_id=course.id,student_id=student.id)
    except:
        ispurchased=None
    
    
    if ispurchased==None:
        new_purchase=PurchaseAndEnrolment(teacher_id=course.teacher_id,student_id=Student.objects.get(id=student.id),course_id=Course.objects.get(id=course.id),amount=course.price)
        new_purchase.save()
    context3 = {'student': student,'ispurchased':ispurchased}
    context = {**context1, **context2,**context3}
    
    
    return render(request, 'base/buynow.html', context)

def teacherRegister(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        address=request.POST['address']
        age=request.POST['age']
        gender=request.POST['gender']
        
        new_Teacher=Teacher(name=name,email=email,password=password,phone=phone,address=address,age=age,gender=gender)
        new_Teacher.save()
        
        return redirect('login')
    
    context={}
    return render(request,'base/student_register.html',context)

def teacherLoginPage(request):
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            teacher = Teacher.objects.get(email=email)
            if teacher.password == password:
                
                    
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
                return redirect('student2fa',teacher.name)

        except:
            messages.error(request, "User Doesn't exist")

    return render(request, 'base/teacher_register_login.html', context)