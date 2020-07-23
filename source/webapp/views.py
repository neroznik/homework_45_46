from django.shortcuts import render

from webapp.models import ToDo_Task


def index_view(request):
    task = ToDo_Task.objects.all()
    return render(request, 'index.html', context={'Tasks': task})

def add_task(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        task = ToDo_Task.objects.all()
        task.task = request.POST.get('task')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.date_proccessing = request.POST.get('data_proccessing')

        task.create()
        print(task)
    return render(request, 'index.html', context={'Tasks': task})

