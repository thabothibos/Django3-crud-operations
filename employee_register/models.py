from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(validators=[RegexValidator(regex=r'^\1?\d{9,10}$')], max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)