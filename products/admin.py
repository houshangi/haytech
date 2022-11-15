from django.contrib import admin
from .models import WareHouse, Category, Product , Order
# Register your models here.
admin.site.register(WareHouse)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
