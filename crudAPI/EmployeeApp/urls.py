# from django.conf.urls import url
# from EmployeeApp import views
# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns = [
#   url(r'^department$', views.departmentApi),
#   url(r'^department/([0-9]+)$', views.departmentApi),

#   url(r'^employee$', views.employeeApi),
#   url(r'^employee/([0-9]+)$', views.employeeApi),

#   url(r'^employee/savefile', views.SaveFile)
# ]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from EmployeeApp.views import MyTokenPairView, RegisterView

router = routers.DefaultRouter()
router.register('departments', views.DepartmentApi, basename='departments')
router.register('employees', views.EmployeeApi, basename='employees')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', MyTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]
