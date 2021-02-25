from django.contrib import admin

# Register your models here.
from .models import customer,product,order
class orderhand(admin.ModelAdmin):
    list_display=['customer_name','product_name','productprice','total_price','quantity']

admin.site.register(customer)
admin.site.register(product)
admin.site.register(order,orderhand)