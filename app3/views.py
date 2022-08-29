from django.shortcuts import render,redirect
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
    context_object_name = "school"
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


# def home(request):
#     return render(request,'homepage.html')
#
# def list_school(request):
#     context = { 'school_list': School.objects.all()}
#     return render(request, 'all_school.html', context)
#
# def list_student(request):
#     context = {'student_list': Student.objects.all()}
#     return render(request, 'all_student.html', context)
#
# def school_details(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             sc_form = SchoolForm()
#         else:
#             school = School.objects.get(pk=id)
#             sc_form = SchoolForm(instance=school)
#
#         return render(request, 'school.html', {'sc_form': sc_form})
#     else:
#         if id == 0:
#             sc_form = SchoolForm(request.POST)
#         else:
#             school= School.objects.get(pk=id)
#             sc_form = SchoolForm(request.POST, instance=school)
#         if sc_form.is_valid():
#             sc_form.save()
#         return redirect('listschool')
#
#
#
#
# def student_details(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             st_form = StudentForm()
#         else:
#             student = Student.objects.get(pk=id)
#             st_form = StudentForm(instance=student)
#         return render(request, 'student.html', {'st_form': st_form})
#     else:
#         if id == 0:
#             st_form = StudentForm(request.POST)
#         else:
#             student = Student.objects.get(pk=id)
#             st_form = StudentForm(request.POST, instance=student)
#         if st_form.is_valid():
#             st_form.save()
#         return redirect('liststudent')


# def school_delete(request, id):
#     school = School.objects.get(pk=id)
#     school.delete()
#     return redirect('listschool')
#
#
# def student_delete(request, id):
#     student = Student.objects.get(pk=id)
#     student.delete()
#     return redirect('liststudent')

