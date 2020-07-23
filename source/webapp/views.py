from django.shortcuts import render

from webapp.models import ToDo_Task


def index_view(request):
    task = ToDo_Task.objects.all()
    print(task)
    return render(request, 'index.html', context={'Tasks': task})

def add_task(request):
    task = ToDo_Task.objects.all()

    if request.method == "POST":
        task.task = request.POST['Task']
        task.description = request.POST['Description']
        task.status = request.POST['Status']
        task.date_proccessing = str(request.POST['Data_proccessing']
        task.save()
    return render(request, 'add.html', context={'Tasks': task})
