from django.contrib import admin
from .models.products import Product
from .models.category import Categorie
from .models.customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email', 'password' ]


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Categorie, AdminCategory)
admin.site.register(Customer, CustomerAdmin)
