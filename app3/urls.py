from django.urls import path
from . import views

urlpatterns=[
    path('',views.Home.as_view(),name="home"),
    path('students/add',views.AddStudent.as_view(),name="addstudent"),
    path("students/all",views.StudentList.as_view(),name="liststudent"),
    path("students/<int:id>", views.StudentDetail.as_view(), name="studentdetail"),
    path("students/change/<int:id>", views.ChangeStudent.as_view(), name="editstudent"),
    path("students/remove/<int:id>", views.StudentDelete.as_view(), name="deletestudent"),
    path('school/add', views.AddSchool.as_view(), name="addschool"),
    path("school/all", views.SchoolList.as_view(), name="listschool"),
    path("school/<int:id>", views.SchoolDetail.as_view(), name="schooldetail"),
    path("school/change/<int:id>", views.ChangeSchool.as_view(), name="editschool"),
    path("school/remove/<int:id>", views.SchoolDelete.as_view(), name="deleteschool"),
    # path('',views.home,name='home'),
    # path('student/list', views.list_student, name='liststudent'),
    # path('school/list', views.list_school, name='listschool'),
    # path('student/add',views.student_details,name='addstudent'),
    # path('school/add', views.school_details, name='addschool'),
    # path("student/remove/<int:id>", views.student_delete, name="deletestudent"),
    # path("school/remove/<int:id>", views.school_delete, name="deleteschool"),
    # path("student/change/<int:id>", views.student_details, name="editstudent"),
    # path("school/change/<int:id>", views.school_details, name="editschool"),

]