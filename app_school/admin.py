from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student, Subject, Teacher

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
