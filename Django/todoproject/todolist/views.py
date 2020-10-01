from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.utils.datastructures import MultiValueDictKeyError

from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request,'home.html',{'tasks':tasks})

# def task_detail(request,task_id):
#     try:
#         task = Task.objects.get(id=task_id)
#     except Task.DoesNotExist:
#         raise Http404('Task not found')    
#     return render(request,'task_detail.html',{'task':task})

def addTask(request):
    if request.method == 'POST':
        todo = Task(task_name=request.POST['content'])
        todo.save()
        return HttpResponseRedirect('/')

def completeTask(request,task):
    if request.method == 'POST':
        todo_del = Task.objects.get(id=task)
        todo_del.delete()
        return HttpResponseRedirect('/')

           
   

