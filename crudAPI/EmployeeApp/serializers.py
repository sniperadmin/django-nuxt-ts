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

class ChangePasswordSerializer(serializers.ModelSerializer):
  old_password = serializers.CharField(
    write_only = True,
    required = True,
  )
  new_password = serializers.CharField(
    write_only = True,
    required = True,
    validators = [validate_password]
  )

  confirm_new_password = serializers.CharField(
    write_only = True,
    required = True,
  )

  class Meta:
    model = User
    fields = ('old_password', 'new_password', 'confirm_new_password')

  def validate(self, attrs):
    if not attrs.get('new_password') != attrs.get('confirm_new_password'):
      raise serializers.ValidationError({
        "password": "Password fields must match"
      })

    return attr

  def validate_old_password(self, value):
    user = self.context.get('request').user
    if not user.check_password(value):
      raise serializers.ValidationError({
        "old_password": "Old password is not correct!"
      })

    return value

  def update(self, instance, validated_data):
    user = self.context.get('request').user

    if user.pk != instance.pk:
      raise serializers.ValidationError({
        "authorize": "You don't have permission for this operation!"
      })

    instance.set_password(validated_data['old_password'])
    instance.save()

    return instance

class UpdateUserSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(required=True)

  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email')
    extra_kwargs = {
      'first_name': { 'required': True },
      'last_name': { 'required': True },
    }

  def validate_email(self, value):
    user = self.context.get('request').user
    if User.objects.exclude(pk=user.pk).filter(email=value).exists():
      raise serializers.ValidationError({
        "email": "This email is already in use"
      })

    return value

  def validate_username(self, value):
    user = self.context.get('request').user
    if User.objects.exclude(pk=user.pk).filter(username=value).exists():
      raise serializers.ValidationError({
        "username": "This username is already in use"
      })

    return value

  def update(self, instance, validated_data):
    user = self.context.get('request').user

    if user.pk != instance.pk:
      raise serializers.ValidationError({
        "authorize": "You don't have permission for this operation!"
      })

    instance.first_name = validated_data['first_name']
    instance.last_name = validated_data['last_name']
    instance.email = validated_data['email']
    instance.username = validated_data['username']

    instance.save()

    return instance

class GetCurrentUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email')

  def get(self, instance):
    user = self.context.get('request').user

    if user.is_authenticated:
      return instance
    else:
      return Response("not auth")
