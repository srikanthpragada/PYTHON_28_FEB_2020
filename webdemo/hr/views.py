from django.shortcuts import render, redirect
from django.http import HttpResponse
import sqlite3
import requests
from .forms import AddEmployeeForm

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


def list_countries(request):
    resp = requests.get("https://restcountries.eu/rest/v2/all")
    countries = resp.json()
    countries = sorted(countries, key=lambda c: c['population'], reverse=True)
    # Calculate total population
    total = 0
    return render(request, 'list_countries.html',
                  {'countries': countries, 'total_population': total})


def add_employee(request):
    if request.method == "POST":
        # process data
        fullname = request.POST['fullname']
        job = request.POST['job']
        salary = request.POST['salary']

        # Connect to db and insert into EMPLOYEES table
        con = sqlite3.connect(r"c:\classroom\feb28\hr.db")
        cur = con.cursor()
        cur.execute("insert into employees (fullname,salary,job) values(?,?,?)",
                    (fullname, salary, job))
        con.commit()  # Commit transaction / Save changes
        con.close()
        return redirect("/hr/employees")
    else:
        return render(request, 'add_employee.html')


def add_employee_with_form(request):
    if request.method == "POST":
        f = AddEmployeeForm(request.POST)  # Bound form
        if f.is_valid():
            fullname = f.cleaned_data['fullname']
            job = f.cleaned_data['job']
            salary = f.cleaned_data['salary']
            # process data
            # Connect to db and insert into EMPLOYEES table
            con = sqlite3.connect(r"c:\classroom\feb28\hr.db")
            cur = con.cursor()
            cur.execute("insert into employees (fullname,salary,job) values(?,?,?)",
                    (fullname, salary, job))
            con.commit()  # Commit transaction / Save changes
            con.close()
            return render(request, 'add_employee_form.html',
                      {'form' : f,  "message" :  "Added Employee Successfully!"})
        else:
            return render(request, 'add_employee_form.html', {'form': f})
    else:
        f = AddEmployeeForm()   #Unbound form
        return render(request, 'add_employee_form.html', {'form' : f})