from django.contrib import admin
from cake_app.models import *


@admin.register(Cake)
class CakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['type']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    list_editable = ['price']


@admin.register(TechCard)
class TechCardAdmin(admin.ModelAdmin):
    list_display = ['model_cake', 'model_product', 'quantity']
    list_editable = ['quantity']
