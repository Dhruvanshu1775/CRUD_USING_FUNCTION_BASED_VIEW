from django.db import models

# Create your models here.

class customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    contact_no = models.CharField(max_length=15)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name
   


class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()

    def __str__(self):
        return self.product_name


class order(models.Model):
    customer_name = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    productprice = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    
    