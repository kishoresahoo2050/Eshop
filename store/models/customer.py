from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField(max_length=100)
    phone = models.BigIntegerField()
    password = models.TextField()

    def __str__(self):
        return self.name
    