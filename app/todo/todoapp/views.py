from django.shortcuts import render,redirect
from todoapp.models import todo


def index(request):
    return render(request, 'index.html')

def add(request):
    if request.method == 'POST':
        name=request.POST['add']
        action=request.POST['action']
        creates=todo.objects.create(task=name,action=action)
        creates.save()
        return redirect('/view/')
    return render(request, 'add.html')

def view(request):
    reads=todo.objects.all().order_by('id')
    return render(request,'view.html',{'reads':reads})   

def edit(request,id):
    edit=todo.objects.get(id=id)
    return render(request,'edit.html',{'edit':edit})

def update(request,id):
    if request.method=="POST":
        task=request.POST['task']
        action=request.POST['action']
        get=todo.objects.get(id=id)
        get.task=task
        get.action=action   
        get.save()
        return redirect('/view/')
    return redirect("/edit/id/")
# if request.method == 'POST':
#     edit.task=request.POST['task']
#     edit.action=request.POST['action']






# from django.shortcuts import render,redirect
# from shashankapp.models import pet_CURD
# # Create your views here.
# def index(request):
#     return render(request, 'index.html')


# def create(request):
#     if request.method == 'POST':
#         name=request.POST['owner']
#         pet=request.POST['pet']
#         create=pet_CURD.objects.create(owner=name,pet=pet)
#         create.save()
#         return redirect('read')
#     return render(request, 'petcreate.html')


# def read(request):
#     reads=pet_CURD.objects.all().order_by('id')
#     return render(request,'read.html',{'reads':reads})

# def edit(request,id):
#     edit=pet_CURD.objects.get(id=id)
#     return render(request,'edit.html',{'edit':edit})

# def update(request,id):
#     if request.method=="POST":
#         owner=request.POST['owner']
#         pet=request.POST['pet']
#         get=pet_CURD.objects.get(id=id)
#         get.owner=owner
#         get.pet=pet     
#         get.save()
#         return redirect('/read/')
#     return redirect("/edit/id/")
#     # if request.method == 'POST':
#     #     edit.owner=request.POST['owner']
#     #     edit.pet=request.POST['pet']

# def delete(request,id):
#     dels=pet_CURD.objects.get(id=id)
#     dels.delete()
#     return redirect('/read/')
