from django.contrib import admin
from .models import Category,Customer,Products,Order
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category,CategoryAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'email', 'phone']
admin.site.register(Customer,CustomerAdmin)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','category','description']
    list_editable = ['name','price','description']
admin.site.register(Products,ProductsAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','product','customer','quantity','price','address','phone','date','status']
admin.site.register(Order,OrderAdmin)