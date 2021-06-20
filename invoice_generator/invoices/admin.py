from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'department_name', 'employee_id', 'name', 'salary', 'joining_date']


admin.site.register(Department)