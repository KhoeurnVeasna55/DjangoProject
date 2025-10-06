from django.db import models

class Student(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Teacher(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
