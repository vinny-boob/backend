from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from.models import*
from . forms import StudentForm

from django.http import HttpResponse 
from . models import *
# Create your views here.

def Home(request):
    return render(request,'MyApp/index.html')

def stdForm(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm()
        context = {'form':form}
    return render(request,'MyApp/stdform.html',context)  


# custom forms


def registStudent(request):
    if request.method == 'POST':
        firstname= request.POST['firstname']
        secondname = request.POST['secondname']
        email = request.POST['email']
        age = request.POST['age']
        regno = request.POST['regno']

        std = student(firstname=firstname, secondname=secondname, email=email, age=age, regno=regno)

        std.save()

        return HttpResponse('success')

    else:
        return render(request,'MyApp/student_form.html')

def retrievestd(request):
    std_data=student.objects.all()
    context={'std_data':std_data}
    return render(request,'MyApp/std_detail.html',context)



def updatestd(request,pk):
    stud=get_object_or_404(student,pk=pk)
    if request.method=='POST':
        new_firstname=request.POST.get('firstname')
        new_lastname=request.POST.get('lastname')
        new_email=request.POST.get('email')
        new_age=request.POST.get('age')
        new_regno=request.POST.get('regno')
        stud.firstname=new_frstname
        stud.lastname=new_lastname
        stud.email=new_email
        stud.age=new_age
        stud.regno=new_regno
        stud.student.save()
        return redirect('fetch_std')
    else:
        context={'stud':stud}
        return render(request,'MyApp/updatestd.html',context)

def deletestd(request,pk):
    del_std=get_object_or_404(student,pk=pk)
    if request.method=='POST':
        del_std.delete()
        return redirect('fetch_std')
    else:
        return render(request,'MyApp/deletestd.html')


def userRegistration(request):
    if request.method=='POST':
        form=customUser(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form=customUser()
    context={'form':form}
    return render(request,'MyApp/regist.html',context)

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        User=authenticate(request,username=username,password=password)
        if User is not None:
            login(request,User)
            return redirect('fetch_std')
    
    return render(request,'MyApp/login.html')
def log_out(request):
    logout(request)
    return redirect('login')








