from django.shortcuts import render
from django.views.generic import View,CreateView,ListView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
# Create your views here.

class Home(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")


class AddStudent(CreateView):
    model = Student
    template_name ="add_student.html"
    form_class = StudentForm
    success_url = reverse_lazy('liststudent')

class StudentDetail(DetailView):
    model = Student
    context_object_name = "student"
    template_name = "student_details.html"
    pk_url_kwarg = "id"


class ChangeStudent(UpdateView):
    model = Student
    template_name = "change_student.html"
    form_class = StudentForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy('liststudent')



class StudentDelete(DeleteView):
    model = Student
    pk_url_kwarg = "id"
    template_name = 'student_delete.html'
    success_url = reverse_lazy('liststudent')

class StudentList(ListView):
    model = Student
    template_name = "student_list.html"
    context_object_name = "students"



class AddSchool(CreateView):
    model = School
    template_name ="add_school.html"
    form_class = SchoolForm
    success_url = reverse_lazy('listschool')

class SchoolDetail(DetailView):
    model = School
    context_object_name = "student"
    template_name = "school_details.html"
    pk_url_kwarg = "id"


class ChangeSchool(UpdateView):
    model = School
    template_name = "change_school.html"
    form_class = SchoolForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy('listschool')



class SchoolDelete(DeleteView):
    model = School
    pk_url_kwarg = "id"
    template_name = 'school_delete.html'
    success_url = reverse_lazy('listschool')

class SchoolList(ListView):
    model = School
    template_name = "school_list.html"
    context_object_name = "schools"

