from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class Company(models.Model):
  name = models.CharField(max_length=255)
  url = models.TextField()

  def __str__(self):
    return self.name

class ProductSize(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=255)
  content = models.TextField()
  category = models.ManyToManyField(Category, related_name='products')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('-created',)

  def __str__(self):
    return self.name

class ProductSite(models.Model):
  name = models.CharField(max_length=255)
  product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    related_name='sites',
    related_query_name='site'
  )
  company = models.ForeignKey(
    Company,
    on_delete=models.CASCADE,
    related_name='sites',
    related_query_name='site',
  )
  product_size = models.ForeignKey(
    ProductSize,
    on_delete=models.CASCADE,
    related_name='sites',
    related_query_name = 'site'
  )
  price = models.DecimalField(max_digits=9, decimal_places=2)
  url = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name

class Comment(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    related_name='comments',
    related_query_name='comment'
  )
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

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
