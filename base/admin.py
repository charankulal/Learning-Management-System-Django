from django.contrib import admin

from .models import Course
from .models import Teacher
from .models import Student
from .models import PurchaseAndEnrolment
from .models import Topic

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(PurchaseAndEnrolment)
admin.site.register(Topic)