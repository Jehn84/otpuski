from django.db import models


class Employee (models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Vacation (models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    vac_start = models.DateField(default="2018-01-01", null=True)
    vac_dur = models.PositiveIntegerField(default=14, null=True)
    vac_end = models.DateField(default="2018-01-14")
    vac_status = models.CharField(max_length=100)


