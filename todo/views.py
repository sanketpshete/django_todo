from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from todo.models import Task

# Create your views here.

def addTask(request):
    new_task = request.POST['Task']
    Task.objects.create(task = new_task)

    return redirect('home')

def mark_as_done(request,pk):
    task = get_object_or_404(Task,pk=pk)

    task.is_completed = True
    task.save()
    return redirect("home")

def mark_as_undone(request,pk):
    task = get_object_or_404(Task,pk=pk)

    task.is_completed = False
    task.updated_at = timezone.now()
    task.save()
    return redirect("home")

def del_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect("home")

def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    

    if request.method == 'POST':
        new_task = request.POST['Task']
        get_task.task = new_task
        get_task.save()

        return redirect("home")
    else:
        context = {
        'get_task':get_task,
        }
        print(get_task)
        return render (request,'edit_task.html',context)