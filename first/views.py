from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Student

# Create your views here.
def index(request):
        stu = Student.objects.all().count()
        count1= Student.objects.all().filter(hno=1).count()
        count2= Student.objects.all().filter(hno=2).count()
        stu1=300-int(stu)
        c1=200-int(count1)
        c2=100-int(count2)
        return render(request, 'index.html',{"stu":stu,"count1":count1,"count2":count2,"stu1":stu1,"c1":c1,"c2":c2})

def login(request):
        if request.method == 'POST' :
                username = request.POST['username']
                password = request.POST['password']  
                user = auth.authenticate(username=username, password=password)      
                if user is not None :
                        auth.login(request,user)
                        return redirect('/')
                else:
                        messages.info(request,'invalid credentials')
                        return redirect('login')
        else:
                return render(request, 'login.html')

def logout(request):
        auth.logout(request)
        return redirect('/')

def table(request):
        stu = Student.objects.all()    
        a1= "ALL STUDENTS"
        return render(request,'table.html', {"stu":stu,"a1":a1 })
        
def shar(request):
        stu= Student.objects.all().filter(hno=1)
        a1="SHARADA"
        return render(request,'shar.html',{"stu":stu,"a1":a1})

def nel(request):
        stu= Student.objects.all().filter(hno=2)
        a1="NELSON MANDELA"
        return render(request,'nel.html',{"stu":stu,"a1":a1})
        
        
