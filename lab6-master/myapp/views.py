from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Student
from .forms import * 
from django.urls import reverse
# Create your views here.

def student_list(request):
    form = StudentForms()
    return render(request ,'student.html' , {"students" :Student.objects.all() ,'forms':form })

def add_student(request):
    print("enter")
    if request.method == "POST":
        form = StudentForms(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('Student') # go back to the list page
        else:
            return render(request,"student.html",{"message":"invalid data"}) # id form in invalid data   
    else:
        return render(request , "student.html" ) # if request is GET 


def courses_list(request):
    form =CoursesForms()
    return render(request , 'courses.html',{"courses_list1":Courses.objects.all() , 'forms':form})

def Add_Course(request):#add coures to the list of courses
    if request.method == "POST":
        form =CoursesForms(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('Courses') # go back to the list page
        else:
            return render(request,"courses.html",{"message":"invalid data"}) # id form in invalid data   
    else:
        return render(request , "courses.html" ) # if request is GET 


def detail(request , Student_id):
    all_courses = Courses.objects.all()
    Student_info = Student.objects.get(id = Student_id)
    corses = Student_info.courses.all()
    unregistered_courses = all_courses.exclude(id__in=corses)
    return render(request , "detail.html" , {'info' : Student_info , "corses":corses ,"none_courses":unregistered_courses})

def add_courses(request , Student_id):#add coures to student
    print("enter")
    if request.method == "POST":
        student_info = Student.objects.get(pk = Student_id)
        course_ids = int(request.POST.getlist('courses')[0])
        print(f" COURSE ID{course_ids}")
        print(f" STUDENT ID{Student_id}")
        student_info.courses.add(course_ids)
    return HttpResponseRedirect(reverse("detail", args=(Student_id,)))   
