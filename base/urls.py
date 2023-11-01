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
    path('teacher/login',views.teacherLoginPage,name='teacherloginpage'),
    path('teacher/register',views.teacherRegister,name='teacherregisterpage'),
    path('teacher/2FA/<str:pk>',views.teacher2FA,name='teacher2fa'),
    path('teacher/main/<str:pk>',views.teacherMainPage,name="teachermain"),
    path('teacher/mycourses/<str:pk>',views.teacherMyCourses,name="teachermycourse"),
    path('teacher/mycourses/<str:sk>/<str:pk>',views.teacherCourseView,name="teachercourseview"),
    path('teacher/mycourses/delete/<str:sk>/<str:pk>',views.deleteCourse,name="teacherdeletecourse"),
    path('teacher/mycourses/students/<str:sk>/<str:pk>',views.studentsEnrolled,name="studentsenrolled"),
    path('teacher/createcourse/<str:pk>',views.teacherCreateCourse,name="createcourse"),
    path('teacher/updatecourse/<str:pk>/<str:sk>',views.teacherUpdateCourse,name="updatecourse"),
    path('teacher/mycourses/delete/<str:sk>/<str:pk>/<str:tk>',views.deleteTopic,name="teacherdeletetopic"),
    path('teacher/mycourses/addtopic/<str:sk>/<str:pk>',views.addTopic,name="addtopic"),
    
]

