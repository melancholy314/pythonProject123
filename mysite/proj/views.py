from django.shortcuts import render
import ast
from django.http import JsonResponse
from . import models
from .models import Student
import sqlite3
# Create your views here.
def proj_view(request):
    return render(request, 'proj/index.html')

def plswork(request):
    query = Student.objects.all()
    print(request)
    return render(request, 'proj/index.html', {"Student":query})

def mygod():
    connection = sqlite3.connect('db.sqlite3')
    print(connection)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM proj_student")
    records = cursor.fetchall()
    num = (len(records))
    return num

def mygodtwo():
    connection = sqlite3.connect('db.sqlite3')
    print(connection)
    cursor = connection.cursor()
    sql = "SELECT * FROM Student"
    cursor.execute(sql)
    records = cursor.fetchall()
    num = (len(records))
    return num
