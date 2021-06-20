from django.shortcuts import render
import xlwt
from django.http import HttpResponse
from datetime import datetime
from .models import *
from xhtml2pdf import pisa
from django.template.loader import get_template



# Create your views here.


def home(request):
    # render Filtered data (eg fullstack developer data)
    # soft = Employee.objects.filter(department_name__name = 'FullStack Developer')

    # render all data
    emp = Employee.objects.all()
    context = {'emp': emp, }
    return render(request, 'index.html', context)


def Download_as_excel(request):
    # specify content_type as ms-excel.
    response = HttpResponse(content_type='application/ms-excel')

    # file name.. attachment means we can download to our local system.
    response['Content-Disposition'] = 'attachment; filename="Employee-Details.xls"'

    # creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    # adding sheet
    ws = wb.add_sheet("sheet1")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()

    # for fetch in date format 
    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/MM/yyyy'

    # headers are bold
    font_style.font.bold = True

    # column header names
    columns = ['Department', 'Employee Id', 'Name', 'Salary', 'Join Date']

    # write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    # get your data, from database...
    data = Employee.objects.all()
    for my_row in data:
        row_num = row_num + 1
        ws.write(row_num, 0, my_row.department_name.name, font_style)
        ws.write(row_num, 1, my_row.employee_id, font_style)
        ws.write(row_num, 2, my_row.name, font_style)
        ws.write(row_num, 3, my_row.salary, font_style)
        ws.write(row_num, 4, my_row.joining_date, date_format)

    wb.save(response)
    return response


def Download_as_PDF(request):
    # Fetch database data what you want...
    data = Employee.objects.all()

    template_path = 'pdf_render.html'
    context = {'data': data}

    # specify content_type as pdf.
    response = HttpResponse(content_type='application/pdf')

    # attachment means we can download to our local system.
    response['Content-Disposition'] = 'attachment; filename="Employee_Details.pdf"'


    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


