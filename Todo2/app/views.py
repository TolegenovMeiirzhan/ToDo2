from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
# Create your views here.
from .models import *


def index(request):
    tasks = Tasks.objects.all()
    context = {"tasks": tasks}
    return render(request, 'app/index.html', context)


def add_todo(request):
    title = request.POST['title']
    new_task = Tasks(title=title)
    new_task.save()
    return HttpResponseRedirect('/')

def complete_todo(request, pk):
    todo_item = Tasks.objects.get(id=pk)
    if todo_item.done == False:
        todo_item.done = True
    else:
        todo_item.done = False
    todo_item.save()
    return HttpResponseRedirect('/')

def delete(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return HttpResponseRedirect('/')

