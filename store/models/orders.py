from django.db import models
from .products import Products
from .customer import Customer
import datetime



class Orders(models.Model):
    product  = models.ForeignKey(Products,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    qty      = models.IntegerField()
    price    = models.DecimalField(max_digits=11,decimal_places=2)
    address  = models.TextField()
    phone    = models.BigIntegerField()
    date     = models.DateField(default=datetime.datetime.today)
    status   = models.BooleanField(default=False)