from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Vacation
from .forms import UserForm
from datetime import timedelta, datetime
import calendar

# получение данных из бд
def index(request):
    c = calendar.HTMLCalendar()
    calendar_year = c.formatyearpage(datetime.today().year, width=3, css='calendar.css', encoding=None)
    result = 0  #переменная для кол-ва пересечений отпусков
    userform = UserForm()
    vacation = Vacation.objects.all()
    for v1 in vacation: #вложенный цикл проверки
        for v2 in vacation:
            if v1.id != v2.id:
                if v2.vac_end >= v1.vac_start > v2.vac_start: #начало первого попадает в промежуток второго
                    result = result + 1
                    v1.vac_status = v1.vac_status + " | " + str(v2.id)
                    v2.vac_status = v2.vac_status + " | " + str(v1.id)
                if v1.vac_start == v2.vac_start: #даты начала отпусков совпадают. прибавляем 0.5 т.к. такое в двойном объеме
                    result = result + 0.5
                    v1.vac_status = v1.vac_status + " | "+str(v2.id)
    return render(request, "core/index.html", {"result": result, "vacation": vacation, "userform": userform, "calendar_year":calendar_year })


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        vacation = Vacation()
        userform = UserForm(request.POST)
        if userform.is_valid():
            vacation.employee = userform.cleaned_data["employee"]
            vacation.vac_start = userform.cleaned_data["vac_start"]
            vacation.vac_dur = userform.cleaned_data["vac_duration"]
            vacation.vac_end = timedelta(userform.cleaned_data["vac_duration"]-1)+userform.cleaned_data["vac_start"]
            #vacation.vac_status = 0
            vacation.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseNotFound("<h2>Введены неверные данные</h2>")
    return HttpResponseRedirect("/")


# изменение данных в бд
def edit(request, id):
    try:
        person = Vacation.objects.get(id=id)
        userform = UserForm(request.POST)
        if request.method == "POST":
            if userform.is_valid():
                person.employee = userform.cleaned_data["employee"]
                person.vac_start = userform.cleaned_data["vac_start"]
                person.vac_dur = userform.cleaned_data["vac_duration"]
                person.vac_end = timedelta(userform.cleaned_data["vac_duration"] - 1) + userform.cleaned_data["vac_start"]
                person.save()
                return HttpResponseRedirect("/")
            else:
                return HttpResponseNotFound("<h2>Введены неверные данные</h2>")
        else:
            return render(request, "core/edit.html", {"person": person, "userform": userform})
    except Vacation.DoesNotExist:
        return HttpResponseNotFound("<h2>Нет такого отпуска</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        person = Vacation.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Vacation.DoesNotExist:
        return HttpResponseNotFound("<h2>Нет такого отпуска. Нечего удалять</h2>")
