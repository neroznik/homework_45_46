from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


BROWSER_DATETIME_FORMAT = '%Y-%m-%d


class TasksForm(forms.Form):
    task = forms.CharField(max_length=100, required=True, label='Задача')
    description = forms.CharField(max_length=1000, required=False, label='Описание', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Статус')
    date_proccessing = forms.DateField(required=True, label='Дедлайн', widget=forms.DateInput(attrs={'type': 'date'}))