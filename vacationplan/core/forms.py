from django import forms
from .models import Employee
from django.contrib.admin.widgets import AdminDateWidget
import datetime

class UserForm(forms.Form):
    employee = forms.ModelChoiceField(Employee.objects.all(), empty_label=None, label="Сотрудник",
        widget=forms.Select(attrs={'class': 'form-control', 'type': 'select'}))
    vac_start = forms.DateField(initial=datetime.date.today(), label="Отпуск с",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    vac_duration = forms.IntegerField(initial=14, label="Дней отпуска", widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'number', 'min': 7, 'max': 14}))
