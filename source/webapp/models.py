from django.utils import timezone
from django.db import models



STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Tasks(models.Model):
    task = models.CharField(max_length=100, null=False, blank=False, verbose_name='Задача')
    description = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Описание')
    status = models.CharField (max_length=50, null=False,choices = STATUS_CHOICES, blank=False, default='new', verbose_name='Статус')
    date_proccessing = models.DateField(default=timezone.now().strftime("%Y-%m-%d"), verbose_name='Дата выполнения', null=False, blank = False)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"


    def __str__(self):
        return "{}. {}".format(self.pk, self.task)


