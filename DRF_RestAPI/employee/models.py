from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name = models.CharField(max_length=30)
    employee_post = models.CharField(max_length=30)
    employee_email = models.EmailField(max_length=30)
    employee_mobile = models.CharField(max_length=10)
    Date_of_joining = models.DateTimeField( auto_now=True)
