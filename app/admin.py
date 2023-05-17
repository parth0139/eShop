from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','city','zipcode','state']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
     list_display=['id','title','selling_price','discounted_price','brand','category','product_image']


@admin.register(Cart)

class CartModelAdmin(admin.ModelAdmin):
     list_display=['id','user','product','quantity']   


@admin.register(OrderPlaced)

class OrderModelAdmin(admin.ModelAdmin):
     list_display=['id', 'user','customer','product','quantity','ordered_date','status']    


@admin.register(contact)

class contact(admin.ModelAdmin):
     list_display=['sno','name','email','phone','time']


