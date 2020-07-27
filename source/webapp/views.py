from django.shortcuts import render, redirect, get_object_or_404

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
        return render(request, 'add.html', context={'status_choices': STATUS_CHOICES})
    elif request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        status = request.POST.get('status')
        date_proccessing = request.POST.get('data_proccessing')
        if date_proccessing != '':
            task = Tasks.objects.create(task=task, description = description, status=status, date_proccessing=date_proccessing)
        else:
            task = Tasks.objects.create(task=task, description=description, status=status)
        return redirect('task_view', pk=task.pk)


