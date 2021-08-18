from django.contrib import admin
from .models import (
  Department,
  Employee,
  Company,
  ProductSize,
  Category,
  Product,
  ProductSite,
  Comment,
)

# Register your models here.
admin.site.register(
  [
    Department,
    Employee,
    Company,
    ProductSize,
    Category,
    Product,
    ProductSite,
    Comment,
  ]
)

# Customize header
admin.site.site_header = 'Basic App'