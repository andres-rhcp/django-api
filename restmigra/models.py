from django.db import models

# User model
class Product(models.Model):
    product_sku = models.CharField(max_length=100,blank=False, default='', primary_key=True)
    product_name = models.CharField(max_length=200,blank=False, default='')
    product_type = models.CharField(max_length=200,blank=False, default='')
    stock = models.IntegerField(blank=False, default='')
    date_update = models.CharField(max_length=100,blank=False, default='')
    user_update = models.CharField(max_length=70,blank=False, default='')
    observation = models.CharField(max_length=200,blank=False, default='') 