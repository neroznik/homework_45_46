from django.shortcuts import render

from webapp.models import ToDo_Task


def index_view(request):
    task = ToDo_Task.objects.all()
    return render(request, 'index.html', context={'Tasks': task})

def add_task(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    elif request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        status = request.POST.get('status')
        date_proccessing = request.POST.get('data_proccessing')
        task = ToDo_Task.objects.create(task=task, description = description, status=status, date_proccessing=date_proccessing)

    return render(request, 'index.html', context={'Tasks': task})

