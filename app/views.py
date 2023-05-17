
# Create your views here.

from django.shortcuts import render,redirect

from django.views import View
from .models import*
from .forms import*

from django.contrib import messages

from django.db.models import Q
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from verify_email.email_handler import send_verification_email


# def index(request): 
#      return render(request,'index.html')

class ProductView(View):
     def get(self,request):
          summer=Product.objects.filter(summer=True)
          winter=Product.objects.filter(winter=True)
          shoe= Product.objects.filter(title='Shoe')
          mobile= Product.objects.filter(category='M')
          laptop= Product.objects.filter(category='L')
          kids= Product.objects.filter(category='k')
          
          if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity
               
               return render(request,'index.html',{'shoe':shoe,'summer':summer,'winter':winter,'mobile':mobile , 'laptop':laptop ,'kids':kids,'element':element})

          


          return render(request,'index.html',{'shoe':shoe,'summer':summer,'winter':winter,'mobile':mobile , 'laptop':laptop ,'kids':kids})
     

class contact(View):

     def get(self,request):
          form=contactForm()

          element=0
          if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               
               for b in cart:
                    element+=b.quantity

          return render(request,'contact.html',{'element':element,'form':form})
     
     def post(self,request):
          
          form=contactForm(request.POST)
          
          if form.is_valid():
               form.save()
               messages.success(request,'Message sent successfully')
               form = contactForm()

          element=0
          if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               
               for b in cart:
                    element+=b.quantity

          return redirect('index') 

          # return render(request,'contact.html',{'element':element,'form':form})               





# def about(request): 

#      if request.user.is_authenticated :
               
#                user=request.user
#                cart= Cart.objects.filter(user=user)
#                element=0
#                for b in cart:
#                     element+=b.quantity
#                return render(request,'about.html',{'element':element})   

#      return render(request,'about.html')




class ProductDetailView(View):
     def get(self,request,pk):
          product=Product.objects.get(pk=pk)

          if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity
               return render(request,'product_detail.html',{'product':product,'element':element})     

          return render(request,'product_detail.html',{'product':product})


def mens(request):
     mens=Product.objects.filter(category='m')

     if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity

               return render(request,'mens.html',{'mens':mens,'element':element})     

     return render(request,'mens.html',{'mens':mens})


def womens(request):
     womens=Product.objects.filter(category='w')

     if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity 

               return render(request,'womens.html',{'womens':womens,'element':element})        

     return render(request,'womens.html',{'womens':womens})

def kids(request):
     kids=Product.objects.filter(category='k')

     if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity

               return render(request,'kids.html',{'kids':kids,'element':element})     

     return render(request,'kids.html',{'kids':kids})

def shoes(request):
     shoes= Product.objects.filter(title='Shoe')

     if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity

               return render(request,'shoes.html',{'shoes':shoes,'element':element})     

     return render(request,'shoes.html',{'shoes':shoes})



def mobile(request,data):
     if data == 'all':
          mobile=Product.objects.filter(category='M')
     
     else :
          mobile=Product.objects.filter(category='M').filter(brand=data)

     if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity          
               
               return render(request,'mobile.html',{'mobile':mobile,'element':element})


     return render(request,'mobile.html',{'mobile':mobile})


def laptop(request,data):
     if data == 'all':
          laptop=Product.objects.filter(category='L')
     
     else :
          laptop=Product.objects.filter(category='L').filter(brand=data)

     if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity

               return render(request,'laptop.html',{'laptop':laptop,'element':element})               

     return render(request,'laptop.html',{'laptop':laptop})




class register(View):
     def get(self,request):
          form =registrationForm()
          return render(request,'register.html',{'form':form})

     def post(self,request):
          form=registrationForm(request.POST)
          if form.is_valid():
               email= form.cleaned_data['email']
               if User.objects.filter(email = email).exists():
                    messages.info(request,'Email already registered')
                    return render(request,'register.html',{'form':form}) 
               
               inactive_user = send_verification_email(request, form)

               
               messages.success(request,"Activate Your Account by clicking the link sent to your email ")
               return redirect("login")
             # return render(request,'email_verify.html')
          return render(request,'register.html',{'form':form}) 



@method_decorator(login_required , name='dispatch')
class profile(View):   
     def get(self,request):
          form = Profile()

          if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity        

          return render(request,'profile.html',{'form':form,'active':'btn-primary','element':element})
     
     def post(self,request):
          form= Profile(request.POST)
          if form.is_valid():
               user=request.user
               name=form.cleaned_data['name']
               phone=form.cleaned_data['phone']
               address=form.cleaned_data['address']
               city=form.cleaned_data['city']
               state=form.cleaned_data['state']
               zipcode=form.cleaned_data['zipcode']
               reg =Customer(user=user,name=name,phone=phone,address=address,city=city,state=state,zipcode=zipcode)
               reg.save()
               form=Profile()
               messages.success(request,'Contratulations!! Profile Updated Succesfully')

          if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity

          return render(request,'profile.html',{'form':form,'active':'btn-primary','element':element})     
     

@login_required     
def address(request):
     add= Customer.objects.filter(user=request.user)

     if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               element=0
               for b in cart:
                    element+=b.quantity

     return render(request,'address.html',{'add':add,'element':element})   


@login_required 
def add_to_cart(request):
       user=request.user
       product_id= request.GET.get('prod_id')
       product= Product.objects.get(id=product_id) 
       if Cart.objects.filter(product=product).exists():
               temp= Cart.objects.get(product=product)
               temp.quantity+=1  
               temp.save()
       else:        
               Cart(user=user,product=product).save()


       cart= Cart.objects.filter(user=user)
       element=0
       for b in cart:
          element+=b.quantity

       return redirect('/cart',{'element',element})

@login_required 
def show_cart(request):
     if request.user.is_authenticated:
         user=request.user
         cart=Cart.objects.filter(user=user)
         amount=0.0
         shipping = 0.0
         total=0.0

         element=0

     #     cart_product=[p for p in Cart.objects.all() if p.user==user]

         if cart:
              for p in cart:
                  amount+=(p.quantity*p.product.discounted_price)

              if amount < 500.0:
                   shipping=50.0

              total=amount+shipping    


              for b in cart:
                    element+=b.quantity 

         return render(request,'cart.html',{'carts':cart,'amount':amount,'shipping':shipping,'total':total,'element':element})
     
@login_required 
def plus_cart(request):
    if request.method == 'GET':
         prod_id = request.GET['prod_id']


         product= Product.objects.get(id=prod_id) 
         c=Cart.objects.get(Q(product=product) & Q( user=request.user))
         
     #     c=Cart.objects.get(Q(product= prod_id) & Q(user=request.user))
         c.quantity+=1
         c.save()
         
         user=request.user
         cart=Cart.objects.filter(user=user)
         amount=0.0
         shipping = 0.0
         total=0.0
         element=0

         if cart:
              for p in cart:
                  amount+=(p.quantity*p.product.discounted_price)

              if amount < 500.0:
                   shipping=50.0

              total=amount+shipping 


               
            
          
              for b in cart:
                    element+=b.quantity

         data={
                   'quantity': c.quantity,
                   'amount':amount,
                   'total':total,
                   'element':element,
                   'shipping':shipping
              }
         return JsonResponse(data)
         
@login_required 
def minus_cart(request):
    if request.method == 'GET':
         prod_id = request.GET['prod_id']

         user=request.user
         product= Product.objects.get(id=prod_id) 
         c=Cart.objects.get(Q(product=product) & Q( user=user))
         
     #     c=Cart.objects.get(Q(product= prod_id) & Q(user=request.user))
         c.quantity-=1
         temp=c.quantity
         if(c.quantity==0):
              c.delete()
          #     return redirect ('/cart')
         else:
              c.save()
         
         user=request.user
         cart=Cart.objects.filter(user=user)
         amount=0.0
         shipping = 0.0
         total=0.0
         
         element=0

         if cart:
              for p in cart:
                  amount+=(p.quantity*p.product.discounted_price)

              if amount < 500.0:
                   shipping=50.0

              total=amount+shipping 


          
              for b in cart:
                    element+=b.quantity


         data={
                   'quantity': temp,
                   'amount':amount,
                   'total':total,
                   'element':element,
                   'shipping':shipping
              }
             
         return JsonResponse(data)
         
                 
@login_required         
def remove_cart(request):
    if request.method == 'GET':
         prod_id = request.GET['prod_id']

         user=request.user
         product= Product.objects.get(id=prod_id) 
         c=Cart.objects.get(Q(product=product) & Q( user=user))
         
     #     c=Cart.objects.get(Q(product= prod_id) & Q(user=request.user))
         
         
         c.delete()
          #     return redirect ('/cart')
         
         user=request.user
         cart=Cart.objects.filter(user=user)
         amount=0.0
         shipping = 0.0
         total=0.0
         
         element=0

         if cart:
              for p in cart:
                  amount+=(p.quantity*p.product.discounted_price)

              if amount < 500:
                   shipping=50.0

              total=amount+shipping 


          
              for b in cart:
                    element+=b.quantity


         data={
                  
                   'amount':amount,
                   'total':total,
                   'element':element,
                   'shipping':shipping
              }
         return JsonResponse(data)
    

@login_required 
def checkout(request):
     user=request.user
     address= Customer.objects.filter(user=user)
     cart=Cart.objects.filter(user=user)
     amount=0.0
     shipping = 0.0
     total=0.0
     element=0
     if cart:
              for p in cart:
                  amount+=(p.quantity*p.product.discounted_price)
                  element+=p.quantity

              if amount < 500   :
                   shipping=50.0

              total=amount+shipping 
     return render(request,'checkout.html',{'address':address,'cart':cart,'total':total,'element':element})


@login_required 
def payment(request):
     user=request.user


     if not request.GET.get('custid'):
          messages.info(request,'Please Select address')
          return redirect('/checkout')
     
     else:

          custid=request.GET.get('custid')
          customer=Customer.objects.get(id=custid)
          cart=Cart.objects.filter(user=user)
          for c in cart:
               OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
               c.delete()
          return redirect ("orders")   



@login_required 
def orders(request):
     op=OrderPlaced.objects.filter(user=request.user)

     cart= Cart.objects.filter(user=request.user)
     element=0
     for b in cart:
         element+=b.quantity 

     return render(request,'orders.html',{'op':op,'element':element})


@login_required 
def buynow(request):
     
          user=request.user

          product_id= request.GET.get('p_id')
     
          product= Product.objects.get(id=product_id)
     
          customer=Customer.objects.filter(user=user)
     
           # OrderPlaced(user=user,customer=customer,product=product,quantity=1).save()
     
          amount= product.discounted_price
          total=amount
          shipping=50.0

          if amount <500:
             total+=shipping

          cart= Cart.objects.filter(user=user)
          element=0
          for b in cart:
              element+=b.quantity        
         

          return render(request,'buy_now.html',{'customer':customer,'b':product,'total':total,'amount':amount,'element':element})



@login_required
def paynow(request):
     user=request.user

     cart= Cart.objects.filter(user=user)
     element=0
     for b in cart:
         element+=b.quantity

     if not request.GET.get('custid'):
          p_id=request.GET.get('bid')
          product=Product.objects.get(id=p_id)
          
          customer=Customer.objects.filter(user=user)
          amount= product.discounted_price
          total=amount
          shipping=50.0

          if amount <500:
             total+=shipping
          messages.info(request,'Please Select address')
          return render(request,'buy_now.html',{'b':product,'customer':customer,'total':total,'amount':amount,'element':element})
     
     else:

          custid=request.GET.get('custid')
          customer=Customer.objects.get(id=custid)
          p_id=request.GET.get('bid')
          product=Product.objects.get(id=p_id)
          
          OrderPlaced(user=user,customer=customer,product=product,quantity=1).save()
               
          return redirect ("orders")        



def search(request):
    q=request.GET['q']

    if q== '':
         return redirect('index')

    data= Product.objects.filter(title__icontains=q).order_by('id')
    category= {}
    if q == "mobile":
         r='M'
         category= Product.objects.filter(category=r).order_by('id')

    elif q== "laptop":
         r='L'
         category= Product.objects.filter(category=r).order_by('id')

    elif q=="mens" or q=="men" :
          r='m'
          category= Product.objects.filter(category=r).order_by('id')

    elif q=="womens" or q=="women" :
          r='w'
          category= Product.objects.filter(category=r).order_by('id')


    element=0
    if request.user.is_authenticated :
               
               user=request.user
               cart= Cart.objects.filter(user=user)
               
               for b in cart:
                    element+=b.quantity        


    return render(request,'search.html',{'data':data,'category':category,'element':element})
     



     
         
                 
               