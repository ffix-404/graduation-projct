from django.db import models

# Create your models here.
class Courses(models.Model):
    courses_name=models.CharField(max_length = 20)
    def __str__(self):
        return f"courses name {self.courses_name}"
class Student(models.Model):# idNumber fname lname email 
    idNumber = models.IntegerField()
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 40)
    courses = models.ManyToManyField(Courses , blank = True , related_name = "students")
    def __str__(self):
        return f"ID NUMBER={self.idNumber} , first name {self.fname} , last name {self.lname} email {self.email} corses{self.courses} "




