from django.db import models

# Create your models here.
class user(models.Model):
    Patient_name=models.CharField(max_length=30)
    Patient_address=models.CharField(max_length=30)
    Phone_No=models.IntegerField()