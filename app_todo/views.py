from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import tasks

# Create your views here.

def index(request):
    layouts_tasks = tasks.objects.order_by('added_date')
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
    new_task.save()
    return render(request, 'index.html', {'added': True})
