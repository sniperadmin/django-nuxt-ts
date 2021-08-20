from rest_framework import viewsets, generics, status
from rest_framework.views import APIView, View
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import renderer_classes, api_view
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, OutstandingToken, BlacklistedToken

from .models import Department,Employee
from .serializers import (
    DepartmentSerializer,
    EmployeeSerializer,
    MyTokenObtainPairSerializer,
    RegisterSerializer,
    ChangePasswordSerializer,
    UpdateUserSerializer,
    GetCurrentUserSerializer
)

from .permissions import IsOwnerOrReadOnly

class DepartmentApi(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeApi(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# This is for login
class MyTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)

class GetCurrentUserView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = GetCurrentUserSerializer
