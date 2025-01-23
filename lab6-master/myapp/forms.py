from django.forms import ModelForm
from .models import *

class StudentForms(ModelForm):
    class Meta:
        model = Student
        fields = ['idNumber','fname' , 'lname','email' ]
class CoursesForms(ModelForm):
    class Meta:
        model = Courses
        fields="__all__"        