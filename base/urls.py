from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.home,name="home"),
    path('course/<str:pk>/',views.courses,name="course"),
    path('login/', views.loginPage, name="login"),
]

