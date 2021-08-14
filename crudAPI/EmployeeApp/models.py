from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class Department(models.Model):
  name = models.CharField(max_length=255, unique=True)
  def __str__(self):
    return self.name

class Employee(models.Model):
  name = models.CharField(max_length=255, unique=True)
  department = models.CharField(max_length=255)
  date_of_joining = models.DateField()
  photo_file = models.CharField(max_length=500)
  # this method for displaying in table
  def __str__(self):
    return self.department
