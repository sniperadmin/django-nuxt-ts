from rest_framework import serializers
from EmployeeApp.models import Department, Employee
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields=['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model=Employee
    fields=['id', 'name', 'date_of_joining', 'department', 'photo_file']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super(MyTokenObtainPairSerializer, cls).get_token(user)

    # custom claims
    token['username'] = user.username
    return token
