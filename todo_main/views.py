
from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    tasks_not = Task.objects.filter(is_completed = False).order_by('-updated_at')
    tasks_done = Task.objects.filter(is_completed = True)

    context = {
        'tasks_not':tasks_not,
        'tasks_done':tasks_done,
    }
    return render(request,'home.html',context)