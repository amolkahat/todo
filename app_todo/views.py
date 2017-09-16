from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

from .models import tasks

# Create your views here.

def index(request):
    layouts_tasks = tasks.objects.filter(state=-1)
    output = [t for t in layouts_tasks]
    if output is not None:
        context = {'list_tasks' : output}
        return render(request, 'index.html', context)
    else:
        context = {'nothing': 'Nothing to print'}
        return render(request, 'index.html', context)

def add_db(request):
    new_task = tasks()
    d = request.POST
    new_task.task_text = d['task_text']
    new_task.added_date = datetime.now()
    new_task.completed_date = datetime.now()
    new_task.save()
    return HttpResponseRedirect('/todo', {'added': True})

def delete_db(request, tid):
    tasks.objects.filter(id=tid).delete()
    return HttpResponseRedirect('/todo', {'deleted': True})

def complete_task(request, tid):
    data = tasks.objects.get(id=tid)
    data.state = 0
    data.save()
    return HttpResponseRedirect('/todo', {'update': True})

def completed(request):
    data = tasks.objects.filter(state=0)
    output = [t for t in data]
    if output is not None:
        context = {'list_tasks': output}
        return render(request, 'completed.html', context)
    else:
        context = {'nothing': 'Nothing to print'}
        return render(request, 'completed.html', context)
