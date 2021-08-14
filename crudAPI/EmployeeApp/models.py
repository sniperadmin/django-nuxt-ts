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

class MyAccountManager(BaseUserManager):
  def create_user(self, email, fullname=None, birthday=None, zipcode=None, password=None):
    if not email:
      raise ValueError("User must have an email address")

    user = self.model(
      email_address = self.normalize_email(email),
      name = self.normalize_email(email),
      date_of_birth = birthday,
      zipcode = zipcode,
    )

    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email_address, password):
    user = self.create_user(
      email_address = self.normalize_email(email_address),
      password = password,
    )

    user.is_admin = True
    user.is_active = True
    user.is_staff = True
    user.is_superuser = True
    user.save(using = self._db)

class User(AbstractBaseUser):
  email_address = models.EmailField(
    verbose_name="email",
    max_length = 255,
    unique = True,
    blank = True,
    null = True,
    default = None,
  )

  name = models.CharField(
    max_length=50,
    unique = True,
    null = True,
  )

  username = models.CharField(
    max_length=50,
    unique = True,
    null = True,
  )

  zipcode = models.CharField(
    max_length=5,
    blank = True,
    null = True,
  )

  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_teacher = models.BooleanField(default=False)
  is_staff = models.BooleanField(default=False)
  is_super_teacher = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  USERNAME_FIELD = 'email_address'

  objects = MyAccountManager()

  class Meta:
    db_table = 'users'

  def __str__(self):
    return str(self.email)

  def has_perm(self, perm, obj=None):
    return self.is_superuser

  def has_module_perms(self, app_label):
    return self.is_superuser
