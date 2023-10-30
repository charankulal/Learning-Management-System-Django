from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.home,name="home"),
    path('course/<str:pk>/',views.courses,name="course"),
    path('login/', views.loginPage, name="login"),
    path('student/main/<str:pk>',views.studentMainPage,name='studentmain'),
    path('student/register',views.studentRegister,name="studentregister"),
    path('student/2FA/<str:pk>',views.student2FA,name="student2fa")
    
]

