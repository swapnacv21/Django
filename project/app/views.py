from django.shortcuts import render,redirect
from django.http import HttpResponse
todo=[{'id':'1','task':'task1'},{'id':'2','task':'task2'},{'id':'3','task':'task3'}]


# Create your views here.
def fun1(request):
    return HttpResponse("Welcome")

def fun2(request):
    return HttpResponse("hello")

def fun3(req,a,b):
    return HttpResponse(a)

def fun4(req,a):
    print(type(a))
    return HttpResponse(a)

def fun5(req,a,b,c):
    if a>b and a>c:
        return HttpResponse(a)
    elif b>a and b>c:
        return HttpResponse(b)
    else:
        return HttpResponse(c)

def index_page(req):
    name='Akhil'
    age=20
    place="ekm"
    return render(req,'index.html',{'name':name,'age':age,'place':place})

def demo(req):
    # l=[1,2,3,4,5,6,7]
    l=[{'name':"Aswin",'age':20},{'name':"Isa",'age':18},{'name':"Jibin",'age':21}]
    d={'name':"Adarsh",'age':23}
    return render(req,"demo.html",{"data":l,'data1':d})

def snd(req):
    return render(req,"second.html")

def fun6(req):
    if req.method=='POST':
        id=req.POST['id']
        task=req.POST['task']
        todo.append({'id':id,'task':task})
        print(todo)
        return redirect(fun6)
    return render(req,'tododisplay.html',{'todo':todo})

def edit(req,id):
    task=''
    for i in todo:
        if i['id']==id:
            task=i
    if req.method=='POST':
        id=req.POST['id']
        task1=req.POST['task']
        task['id']=id
        task['task']=task1
        return redirect(fun6)
    return render(req,'edit.html',{'task':task})


def delete(req,id):
    for i in todo:
        if i['id']==id:
            todo.remove(i)
    return redirect(fun6)