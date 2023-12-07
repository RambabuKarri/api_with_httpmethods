from django.db import models

# Create your models here.
class Employe(models.Model):
    
    Ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    sal=models.IntegerField()

class Productdata(models.Model):
    category=models.CharField(max_length=100)
    

class Product(models.Model):
    category=models.ForeignKey(Productdata,on_delete=models.CASCADE)
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    

