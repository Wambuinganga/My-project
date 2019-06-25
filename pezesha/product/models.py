from django.db import models
from user.models import User

class Product(models.Model):
	product_name=models.CharField(max_length=60)
	image=models.ImageField(upload_to='profile_image',blank=True)
	description=models.TextField(blank=True)
	user=models.ForeignKey(User, related_name='products',on_delete=models.PROTECT)

def __str__(self):
	return self.product_name
			

# upload_to='products/%Y/%m/%d',