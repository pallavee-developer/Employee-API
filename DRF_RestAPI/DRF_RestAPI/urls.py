from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from employee.viewset import EmployeeViewset

router =routers.DefaultRouter()
router.register(r'emps',EmployeeViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
