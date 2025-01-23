from django.urls import path
from . import views
urlpatterns=[
    path("Student",views.student_list,name="student page"),# student path
    path("1",views.add_student , name="add student"),

    path("Courses" , views.courses_list ,name = "courses page"),#courses path
    path("2" , views.Add_Course , name="add course"),

    path("<int:Student_id>",views.detail , name = "detail"),#detail path
    path("<int:Student_id>/add", views.add_courses , name = 'add course')
    
]