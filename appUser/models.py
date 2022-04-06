from django.db import models

# Create your models here.
class AppUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstName = models.CharField(max_length=14)
    lastName = models.CharField(max_length=14)
    email = models.CharField(unique=True, max_length=25)
    userName = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10)
    passWord = models.CharField(max_length=20)



