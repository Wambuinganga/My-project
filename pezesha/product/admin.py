from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display=("image","product_name", "description")
	search_fields=("product_name",)

admin.site.register(Product, ProductAdmin)

