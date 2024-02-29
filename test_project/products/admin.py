from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
