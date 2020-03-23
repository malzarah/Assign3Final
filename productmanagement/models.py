from django.db import models
from django.urls import reverse
# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=50, )
    address = models.CharField(max_length=26, null=True)
    city = models.CharField(max_length=26, null=True)
    state = models.CharField(max_length=26, null=True)
    zip = models.CharField(max_length=6, null=True)
    notes = models.TextField(max_length=255, null=True)

    # def __str__(self):
    #     return self.location

    def get_absolute_url(self):
        return reverse('location', args=[str(self.id)])



class Customer(models.Model):
    first_name=models.CharField(max_length=50, )
    last_name=models.CharField(max_length=50, )
    city = models.CharField(max_length=26, null=True)
    state = models.CharField(max_length=26, null=True)
    zip = models.CharField(max_length=6, null=True)
    notes = models.TextField(max_length=255, null=True)

    # def __str__(self):
    #     return self.Customer

    def get_absolute_url(self):
        return reverse('location', args=[str(self.id)])


class Product(models.Model):
    product_name=models.CharField(max_length=50, )
    product_manufacturer=models.CharField(max_length=50, )


    # def __str__(self):
    #     return self.location

    def get_absolute_url(self):
        return reverse('location', args=[str(self.id)])