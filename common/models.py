from django.db import models

# Create your models here.

class Customer(models.Model):
    Customer_name = models.CharField(max_length=20)
    Email_address = models.CharField(max_length=30)
    Address = models.CharField(max_length=50)
    Phone_number = models.BigIntegerField()
    Gender = models.CharField(max_length=50)
    Cust_password = models.CharField(max_length=10)

class Seller(models.Model):
    seller_name = models.CharField(max_length=20)
    seller_email = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Phone_number = models.BigIntegerField()
    Gender = models.CharField(max_length=50)
    comp_name = models.CharField(max_length=100)
    accholder_name = models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)
    branch = models.CharField(max_length=20)
    seller_user = models.CharField(max_length=20)
    seller_pass = models.CharField(max_length=20)
    acc_number = models.BigIntegerField()
    sell_pic = models.ImageField(upload_to='seller/')



