from django.shortcuts import render
from django.http import HttpResponse
import sqlite3


# Create your views here.


def welcome(request):
    return HttpResponse("<h1>Welcome to Human Resources</h1>")


def index(request):
    return render(request, 'index.html')


def list_employees(request):
    con = sqlite3.connect(r"c:\classroom\feb28\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees")
    emps = cur.fetchall()
    con.close()
    return render(request, 'list_employees.html', {'employees': emps})
