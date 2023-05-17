

from django.db import models
from django.utils import *
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator,MinValueValidator 

from phonenumber_field.modelfields import PhoneNumberField

# from location_field.models.plain import PlainLocationField

state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))

class Customer(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     name=models.CharField(max_length=50)
     city=models.CharField(max_length=50)
     address=models.CharField(max_length=200)
    #  location = PlainLocationField(based_fields=['city'], zoom=7)
     
     zipcode=models.IntegerField()
     phone= PhoneNumberField(blank=True)
     state=models.CharField(choices=state_choices,max_length=50)

     def __str__(self):
        return str(self.id)
     
category_choices= (
    ('M','Mobile'),
    ('L','Laptop'),
    ('m','Mens'),
    ('w','Womens'),
    ('k','Kids'),
    
)

sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )

    
# seasons=(
#        ('s','summer'),
#        ('w','winter')
#     )


class Product(models.Model):

    title= models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description=models.TextField()
    brand= models.CharField( max_length=50)
    category= models.CharField(choices=category_choices,max_length=2)
    product_image=models.ImageField(upload_to='product_img')
    summer=models.BooleanField(default=False)
    winter=models.BooleanField(default=False)
    top_wear=models.BooleanField(default=False)
    botton_wear=models.BooleanField(default=False)
   
    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user= models.ForeignKey(User,on_delete= models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=1, choices=sizes,default='S')

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
       
    

status_choices=(('Accepted','Accepted'),
                ('Packed','Packed'),
                ('On the Way','On the Way'),
                ('Delivered','Delivered'),
                ('Cancel','Cancel'),
                ('Pending','Pending')
)

class OrderPlaced(models.Model):
    user= models.ForeignKey(User,on_delete= models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer,on_delete= models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=status_choices,default='Pending') 

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    

class contact(models.Model):
     sno= models.AutoField(primary_key=True)
     name=models.CharField(max_length=55)
     email=models.EmailField(max_length=100)
     phone=PhoneNumberField(blank=True)
     content=models.TextField()
     time= models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return 'Message from '+ ' '+self.name + ' '+self.email    