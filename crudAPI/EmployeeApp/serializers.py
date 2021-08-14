from rest_framework import serializers
from EmployeeApp.models import Department, Employee
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
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

class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )

  password = serializers.CharField(
    write_only=True,
    required=True,
    validators=[validate_password]
  )

  confirm_password = serializers.CharField(
    write_only=True,
    required=True
  )

  class Meta:
    model = User
    fields = (
      'username',
      'password',
      'confirm_password',
      'email',
      'first_name',
      'last_name',
    )

    # We can add extra custom validation like so:
    extra_kwargs = {
      'first_name': { 'required': True },
      'last_name': { 'required': True },
    }

  def validate(self, attrs):
    if attrs.get('password') != attrs.get('confirm_password'):
      raise serializers.ValidationError({
        "password": "Password fields didn't match!"
      })

    return attrs

  def create(self, validated_data):
    user = User.objects.create(
      username = validated_data['username'],
      email = validated_data['email'],
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name'],
    )

    user.set_password(validated_data['password'])
    user.save()

    return user
