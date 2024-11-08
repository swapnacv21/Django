from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    product_id=models.TextField()
    product_name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)



# model for view booked product details :
# class Buy(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    # product=models.ForeignKey(Product,on_delete=models.CASCADE)
    # price=models.IntegerField()
    # date=models.DateField(auto_now_add=True)
    # ----------------------> after this ---> makemigrations--->migrate------>runserver