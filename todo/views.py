from django.urls import reverse
import email
from glob import glob
from unicodedata import name
from django.shortcuts import redirect, render,HttpResponse

from .models import Task
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
# Create your views here.
mail = ""


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    return render(request,'login.html')

def user_logout(request):
    if request.user.is_authenticated:
    
        logout(request)
        return redirect('/')

@csrf_protect
def signup(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == "POST":
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        users = User.objects.filter(username=username,email=email)
        auth_user = authenticate(username=username)
        if len(users) > 0:
            messages.error(request,"User already exist please login!")
        else:
            if len(password) <7:
                messages.error(request,'Password length should be greater than 8!')
            else:
                try:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    login(request,user) 
                except Exception as e:
                    messages.error(request,"Username not available. Try unique username!")
                    # return redirect(request,'/signup')
            # try:
            #     user = User.objects.create_user(username=username,email=email,password=password)
            #     user.save()
            #     login(request,user) 
            # except Exception as e:
            #     messages.error(request,"Username not available!")
            #     return redirect(request,'/signup')
        # newuser = User(name=name,email=email,password=password)
        # global mail
        # mail = email
        return redirect('/home/')
    return render(request,'signup.html')

@csrf_protect
def loginn(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # usercheck = User.objects.filter(email=email)
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("/home/")
        else:
            messages.error(request,"Invalid crediantial please try again or signup!")
            return redirect('/login/')
        # userpasscheck = User.objects.filter(password = password)
        # if len(usercheck) !=0 and len(userpasscheck) != 0:
        #     global mail
        #     mail = email
        #     return redirect('/home/')
        # else:
        #     return render(request,'login.html',{'msg':'Entered wrong email or password!'})
    return render(request,'login.html')

def home(request):
    if request.method =="POST":
        # user = request.POST.get('email')
        # newtask = request.POST.get('task')
        removetask = request.POST.get('rmtask')
        print(removetask)
        if removetask != '':
            rmtask = Task.objects.filter(number=removetask)
            # print(rmtask)
            if len(rmtask) > 0:
                rmtask.delete()
        if removetask is None:
            newtask = request.POST.get('task')
            createtast = Task(username=request.user,task=newtask)
            createtast.save()
            # return redirect(request,'/savetask/')
    if request.user.is_authenticated:
        task = Task.objects.filter(username=request.user)
        # print(task)
        if len(task) > 0:
            return render(request,'home.html',{'tasks':task})
        else:
            return render(request,'home.html',{'msg':"No tasks found please create some task!"})
    else:
        # return print('error')
        print()
        return redirect("/")
       

    
    
    
    
    
    
    
    
def match(alltaks,query):
    if query in alltaks.task.lower() or query in alltaks.task.upper() or query in str(alltaks.date) and alltaks.email == mail:
        return True
    else:
        False
def search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        alltaks = Task.objects.filter(username=request.user)
        sorted = [task for task in alltaks if match(task,query.lower())]
        return render(request,'search.html',{'tasks':sorted})
        
    return render(request,'search.html')