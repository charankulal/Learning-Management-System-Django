from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.home,name="home"),
    path('course/<str:pk>/',views.courses,name="course"),
    path('student/course/<str:sk>/<str:pk>',views.studentCourses,name="studentcourse"),
    path('student/mycourse/<str:pk>',views.studentMyCourses,name="studentmycourse"),
    path('login/', views.loginPage, name="login"),
    path('student/main/<str:pk>',views.studentMainPage,name='studentmain'),
    path('student/register',views.studentRegister,name="studentregister"),
    path('student/2FA/<str:pk>',views.student2FA,name="student2fa"),
    path('student/mycourse/<str:sk>/<str:pk>',views.studentMyCourseStudy,name="studentmycoursestudy"),
    path('student/course/buynow/<str:sk>/<str:pk>',views.studentBuyCourse,name='buynow'),
    path('teacher/login',views.teacherLoginPage,name='teacherloginpage')
    
]

