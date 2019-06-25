from django.shortcuts import render
from .forms import ProductForm
from .models import Product

# def add_product(request):
# 	if request.method=="POST":
# 		form=ProductForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 	else:
# 		form =ProductForm()
# 	return render(request, "add_product.html", {"form":form})
	
def list_products(request):
	products=Product.objects.all()
	return render(request, "list_products.html",{"products":products})
	# Create your views here.
