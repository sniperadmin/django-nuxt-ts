from rest_framework import viewsets
# from api.permissions import ReadOnly
from .models import Department,Employee
from .serializers import DepartmentSerializer, EmployeeSerializer

class departmentApi(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class employeeApi(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
