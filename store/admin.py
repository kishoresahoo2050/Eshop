from django.contrib import admin
from .models.products import Products
from .models.category import Category
from .models.customer import Customer
# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','category','name','price','img']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','email']
