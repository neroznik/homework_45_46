from django import forms
from .models import Status, Types

default_status = Status.status['new']
default_type = Types.types['task']


BROWSER_DATETIME_FORMAT = '%Y-%m-%d'


class TasksForm(forms.Form):
    task = forms.CharField(max_length=100, required=True, label='Задача')
    description = forms.CharField(max_length=1000, required=False, label='Описание', widget=forms.Textarea)
    status = forms.ChoiceField(choices=Status.status, initial=default_status, label='Статус')
    type = forms.ChoiceField(choices=Types.types, initial=default_type, label='Тип')
    created_at = forms.DateField(required=True, label="Дедлайн", widget=forms.DateInput(attrs={'type': 'date'}))