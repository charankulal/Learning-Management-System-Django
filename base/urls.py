from django.urls import path
from . import views

app_name='base'

urlpatterns = [
    path('',views.home,name="home"),
    path('course/<str:pk>/',views.courses,name="course")
]

