from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser

from .views import departmentApi, employeeApi
from .models import Department, Employee

# Create your tests here.
class DepartmentModelTest(TestCase):
  def setUp(self):
    Department.objects.create(name = "test name").save()
  
  def test_name_label(self):
    dep = Department.objects.get(name='test name')
    self.assertEqual(f'{dep.name}', 'test name')
    print("dep is ... => ", dep)

  # def test_name_max_length(self):
  #   new_dep_name = 'x' * 356
  #   print("new name => ", new_dep_name)
  #   new_dep = Department.objects.create(name=new_dep_name).save()
  #   with self.assertRaises():
  #     new_dep.full_clean()

class ViewsTest(TestCase):
  # def setUp(self):
  #   self.factory = requestFactory()
  #   self.user = User.objects.create_user(
  #     username='nash', email='nash@gmail.com', password='meow'
  #   )

  def test_department_api_endpoints(self):
    get_request = self.client.get('/api/departments/')
    self.assertEqual(get_request.status_code, 200)

  def test_employee_api_endpoints(self):
    get_request = self.client.get('/api/employees/')
    self.assertEqual(get_request.status_code, 200)
