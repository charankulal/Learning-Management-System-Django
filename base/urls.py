from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Home"),
    path('courses/<str:pk>/',views.courses,name="Courses")
]

