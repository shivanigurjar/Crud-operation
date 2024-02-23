from django.db import models

# Create your models here.
class your_model(models.Model):
    First_name=models.CharField(max_length=55)
    Last_name=models.CharField(max_length=55, null="True")
    Password=models.CharField(max_length=100)