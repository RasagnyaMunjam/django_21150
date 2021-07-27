from django.db import models

# Create your models here.
class User(models.Model):
    S.No = models.IntegerField(max_length=70)
    Patientname = models.CharField(max_lengty=70)
    email=models.EmailField(max_length=70)
    Phonenumber = models.CharField(max_length=70)

