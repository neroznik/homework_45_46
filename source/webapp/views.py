from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import make_naive

from webapp.forms import TasksForm, BROWSER_DATETIME_FORMAT
from webapp.models import Tasks, STATUS_CHOICES


def index_view(request):
    task = Tasks.objects.all()
    return render(request, 'index.html', context={'Tasks': task})

def tasks_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    context = {'Tasks': task }
    return render(request, 'task_view.html', context)



def add_task(request):
    if request.method == 'GET':
        return render(request, 'add.html', context={'form': TasksForm})
    elif request.method == 'POST':
        form = TasksForm(data=request.POST)
        if form.is_valid():
            task = Tasks.objects.create(**form.cleaned_data)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'add.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])



def task_update_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == "GET":
        form = TasksForm(initial={
            'task': task.task,
            'description': task.description,
            'status': task.status,
            'date_proccessing': task.date_proccessing
        })
        return render(request, 'task_update.html', context={
            'form': form,
            'Tasks': task
        })
    elif request.method == 'POST':
        form = TasksForm(data=request.POST)
        if form.is_valid():
            Tasks.objects.filter(pk=pk).update(**form.cleaned_data)
            Tasks.save()
            return redirect('task_view', pk=Tasks.pk)
        else:
            return render(request, 'task_update.html', context={
                'Tasks': task,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def task_delete_view(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    if request.method == 'GET':
        return render(request, 'tasks_delete.html', context={'Tasks': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])