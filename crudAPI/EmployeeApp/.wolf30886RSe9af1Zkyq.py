from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def departmentApi(request, id = 0):
  if request.method == 'GET':
    departments = Departments.objects.all()
    departments_serializer = DepartmentSerializer(departments, many=True)
    return JsonResponse(departments_serializer.data, safe=False)

  elif request.method == 'POST':
    department_data = JSONParser().parse(request)
    departments_serializer = DepartmentSerializer(data = department_data)

    if departments_serializer.is_valid():
      departments_serializer.save()
      return JsonResponse("Added record successfully => " + departments_serializer.data, safe = False)

    return JsonResponse("Error adding record to database!", safe=False)

  elif request.method == 'PUT':
    department_data = JSONParser().parse(request)
    department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
    departments_serializer = DepartmentSerializer(deparment, data = department_data)

    if departments_serializer.is_valid():
      departments_serializer.save()
      return JsonResponse("Added record successfully!", safe = False)
    return JsonResponse("Error Editing record!", safe = False)

  elif request.method == 'DELETE':
    department = Departments.objects.get(DepartmentId = id)
    department.delete()
    return JsonResponse("Deleted record successfully!", safe = False)

# employees
@csrf_exempt
def employeeApi(request, id = 0):
  if request.method == 'GET':
    employees = Employees.objects.all()
    employees_serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(employees_serializer.data, safe=False)

  elif request.method == 'POST':
    employee_data = JSONParser().parse(request)
    employees_serializer = EmployeeSerializer(data = employee_data)

    if employees_serializer.is_valid():
      employees_serializer.save()
      return JsonResponse("Added record successfully => " + employees_serializer.data, safe = False)

    return JsonResponse("Error adding record to database!", safe=False)

  elif request.method == 'PUT':
    employee_data = JSONParser().parse(request)
    employee = Employees.objects.get(EmployeeId=employee_data['employeeId'])
    employees_serializer = EmployeeSerializer(employee, data = employee_data)

    if employees_serializer.is_valid():
      employees_serializer.save()
      return JsonResponse("Added record successfully!", safe = False)
    return JsonResponse("Error Editing record!", safe = False)

  elif request.method == 'DELETE':
    employee = employees.objects.get(employeeId = id)
    Employee.delete()
    return JsonResponse("Deleted record successfully!", safe = False)

@csrf_exempt
def save_file(request):
  file = request.FILES['file']
  file_name = default_storage.save(file.name, file)
  return JsonResponse(file_name, safe = False)
