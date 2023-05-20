#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import requests
import psycopg2

def employee_list(request):
    # employees = Employee_Profiles.objects.all()
    # return render(request, 'employee_list.html', {'employees': employees})
    a=json.loads(request.body)
    b=a['id']
    Emp_Prof = Employee_Profiles.objects.get(pk=b)
    
    Name=str(Emp_Prof.First_Name)
    First_Name = str(Emp_Prof.First_Name)
    Last_Name = str(Emp_Prof.Last_Name)
    Email = str(Emp_Prof.Email)
    Phone = int(Emp_Prof.Phone)
    Dob = str(Emp_Prof.Dob)
    Blood_Group = str(Emp_Prof.Blood_Group)
    
    Emp_Prof.First_Name = First_Name
    Emp_Prof.Last_Name = Last_Name
    Emp_Prof.Email = Email
    Emp_Prof.Phone = Phone
    Emp_Prof.Dob = Dob
    Emp_Prof.Blood_Group = Blood_Group
    Name = Emp_Prof.add_name()
    
    Emp_Prof.save()
    resposne = {Name : True}
    return JsonResponse(resposne)
    
    