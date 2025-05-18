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