from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.TextField()
    product_name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()