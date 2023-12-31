from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password=models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password=models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    age=models.CharField(max_length=10)
    gender=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Course(models.Model):
    courseName = models.CharField(max_length=200)
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    description=models.TextField()
    content=models.TextField()
    price=models.CharField(max_length=10)
    category=models.CharField(max_length=200)
    
    def __str__(self):
        return self.courseName
    
class PurchaseAndEnrolment(models.Model):
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    amount=models.CharField(max_length=10)
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.amount
    
class Topic(models.Model):
    teacher_id=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course_id=models.ForeignKey(Course,on_delete=models.CASCADE)
    content=models.TextField()
    updated_at=models.DateTimeField(auto_now=True)
    published_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content
    
