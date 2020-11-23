from django.contrib import admin
from .models import (
    ProductInfo,
    Product,
    SubCategory,
    Category,
    Booking
)

models_list = [ProductInfo, SubCategory, Category, Booking, Product]
admin.site.register(models_list)
