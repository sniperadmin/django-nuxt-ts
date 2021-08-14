from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class Department(models.Model):
  name = models.CharField(max_length=255, unique=True)

  # employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Employee(models.Model):
  name = models.CharField(max_length=255, unique=True)
  date_of_joining = models.DateField()
  photo_file = models.CharField(max_length=500, null=True, blank=True)

  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  # this method for displaying in table
  def __str__(self):
    return self.department
