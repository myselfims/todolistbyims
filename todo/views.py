from unicodedata import name
from django.shortcuts import redirect, render,HttpResponse
from numpy import number
from .models import Task,User
# Create your views here.
loginn = False

def login(request):
    if request.method == "POST":
        print("hello")
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User(name=name,email=email,password=password)
        user.save()
        global login
        login = True
        return redirect(request,'/home')
    return render(request,'login.html')
print(login)

def home(request):
    # global login
    # if login != True:
    #     return render(request,'login.html')
        
    if request.method == "POST":
        task = request.POST.get('task')
        print(type(task))
        rmtask = request.POST.get('rmtask')
        deltask = Task.objects.filter(number=rmtask)
        deltask.delete()
        alltask = Task.objects.all()
        print(len(alltask))
        if task == None:
            pass
        elif task != "":
            tasks = Task(task=task)
            tasks.save()
        else:
            return HttpResponse('error')
        
        
    
        # return render(request,'home.html')
    tasks = Task.objects.all()
    if len(tasks) == 0:
         return render(request,'home.html',{'msg':'Tasks not available create some tasks!'})
    return render(request,'home.html',{'tasks':tasks})
def match(alltaks,query):
    if query in alltaks.task.lower() or query in alltaks.task.upper() or query in str(alltaks.date):
        return True
    else:
        False
def search(request):
    print("yaha aara")
    if request.method == "GET":
        print("yaha aara")
        query = request.GET.get('query')
        print(query)
        alltaks = Task.objects.all()
        print(alltaks)
        sorted = [task for task in alltaks if match(task,query)]
        print(sorted)
        return render(request,'search.html',{'tasks':sorted})
        
    return render(request,'search.html')