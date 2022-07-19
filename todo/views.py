import email
from glob import glob
from unicodedata import name
from django.shortcuts import redirect, render,HttpResponse
from numpy import number
from .models import Task,User
# Create your views here.
mail = ""


def loginpage(request):
    return render(request,'login.html')

def logout(request):
    if request.method == "POST":
        global mail
        mail = ""
        return redirect('/')

def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        newuser = User(name=name,email=email,password=password)
        newuser.save()
        global mail
        mail = email
        return redirect('/home/')
    return render(request,'signup.html')

def login(request):
    global mail
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usercheck = User.objects.filter(email=email)
        userpasscheck = User.objects.filter(password = password)
        if len(usercheck) !=0 and len(userpasscheck) != 0:
            global mail
            mail = email
            return redirect('/home/')
        else:
            return render(request,'login.html',{'msg':'Entered wrong email or password!'})
    return render(request,'login.html')

def home(request):
    global mail
    # if login != True:
    #     return render(request,'login.html')
        
    if request.method == "POST":
        task = request.POST.get('task')
        email = request.POST.get('email')
        rmtask = request.POST.get('rmtask')
        deltask = Task.objects.filter(number=rmtask)
        deltask.delete()
        alltask = Task.objects.all()
        if task == None:
            pass
        elif task != "":
            tasks = Task(task=task,email=mail)
            tasks.save()
        else:
            return HttpResponse('error')
        
        
    # global mail
    tasks = Task.objects.filter(email=mail)
    user = User.objects.filter(email=mail)
    if mail != "":
        if len(tasks) == 0:
            return render(request,'home.html',{'msg':'Tasks not available create some tasks!'})
        return render(request,'home.html',{'tasks':tasks,'user':user})
    else:
        return redirect('/')
def match(alltaks,query):
    if query in alltaks.task.lower() or query in alltaks.task.upper() or query in str(alltaks.date) and alltaks.email == mail:
        return True
    else:
        False
def search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        global mail
        alltaks = Task.objects.filter(email=mail)
        sorted = [task for task in alltaks if match(task,query.lower())]
        return render(request,'search.html',{'tasks':sorted})
        
    return render(request,'search.html')