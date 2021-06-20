from django.db import models

from datetime import date 
from django.utils import timezone


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


class Employee(models.Model):
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee_id = models.IntegerField()
    name = models.CharField(max_length=20)
    salary = models.IntegerField()
    joining_date = models.DateField()
    