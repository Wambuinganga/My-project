from django.db import models


class User(models.Model):
    full_names= models.CharField(max_length=50)
    # user_name=models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)

    def __str__(self):
        return self.full_names

    def shop_products(self):
        return self.products.all
 
    