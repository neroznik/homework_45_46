from django.utils import timezone
from django.db import models


class ToDo_Task(models.Model):
    status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]

    task = models.CharField(max_length=100, null=False, blank=False, verbose_name='Задача')
    description = models.TextField(max_length=500, null=False, blank=True, verbose_name='Описание')
    status = models.CharField (max_length=50, null=False,choices= status_choices, blank=False, default= 'new', verbose_name='Статус')
    date_proccessing = models.DateField(default=timezone.now().strftime("%Y-%m-%d"), verbose_name='Дата выполнения', blank = False)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


    def __str__(self):
        return "{}. {}".format(self.pk, self.task)

