from rest_framework import serializers
from EmployeeApp.models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields=['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model=Employee
    fields=['id', 'name', 'date_of_joining', 'department', 'photo_file']
