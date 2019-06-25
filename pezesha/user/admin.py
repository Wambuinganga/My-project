from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
	list_display=("full_names", "email","password")
	search_fields=("full_names","email")
	

admin.site.register(User)
