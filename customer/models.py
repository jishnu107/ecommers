from django.db import models
from prodseller.models import Product
from common.models import Customer


# Create your models here.

class Cart(models.Model):
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    customer =  models.ForeignKey(Customer, on_delete=models.CASCADE)
