from django.http import HttpResponse
from django.shortcuts import redirect, render
from todo.models import Task

# Create your views here.

def addTask(request):
    new_task = request.POST['Task']
    Task.objects.create(task = new_task)

    return redirect('home')