from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator
# Create your models here.


class Student(models.Model):
     lfno = models.IntegerField(primary_key=True)
     name = models.CharField(max_length=30)
     program = models.CharField(max_length=10)
     phone = PhoneNumberField(unique=True, max_length=13, validators=[MinLengthValidator(10)])
     email = models.EmailField(max_length=50)
     hno= models.IntegerField()
     roomno = models.IntegerField()

class Hostel(models.Model):
     hno = models.IntegerField(primary_key=True)
     hname = models.CharField(max_length=15)
     sharing = models.IntegerField()
 
