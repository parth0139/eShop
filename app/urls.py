

from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from .views import *
from app import views

from django.contrib.auth import views as auth_view
from .forms import *

urlpatterns = [
    # path('',index,name='index'),

    path('', views.ProductView.as_view(),name='index'),

    path('contact/',views.contact.as_view(),name='contact'),
    # path('about/',about,name='about'),
    path('accounts/login/',auth_view.LoginView.as_view(template_name='login.html',authentication_form=login) ,name='login'),

    path('logout/',auth_view.LogoutView.as_view(next_page='login') ,name='logout'),


    path('register/',views.register.as_view(),name='register'),


    # path('product/<int:pk>',product_detail,name='product-detail'),

    path('product/<int:pk>', views.ProductDetailView.as_view() , name='product-detail'),
    path('mobile/<slug:data>', mobile ,name='mobiledata'),
    
    path('laptop/<slug:data>', laptop ,name='laptop'),
    path('mens/', mens ,name= 'mens' ),

    path('womens/', womens ,name= 'womens' ),
    path('kids/', kids ,name= 'kids' ),
    path('shoes/', shoes ,name= 'shoes' ),

     path('passwordChange/', auth_view.PasswordChangeView.as_view(template_name='password.html',form_class=passwordchange , success_url='/passwordchanged/' ),name='password'),


    path('passwordchanged/',auth_view.PasswordChangeDoneView.as_view( template_name='passwordchanged.html'),name='passwordchanged' ),

 path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=passswordreset), name='reset' ),

 path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done' ),

 path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class= setpassword ), name='password_reset_confirm' ),

 path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete' ),

path('address/', address, name='address'),

path('profile/', views.profile.as_view() ,name='profile' ),

path('add-to-cart/', add_to_cart ,name='add-to-cart'),

path('cart/', show_cart ,name='showcart'),

path('pluscart/', plus_cart ,name='pluscart'),

path('minuscart/', minus_cart ,name='minuscart'),

path('removecart/', remove_cart ,name='removecart'),

path('checkout/', checkout ,name='checkout'),

path('payment/', payment ,name='payment'),

path('orders/', orders ,name='orders'),

path('buy-now/', buynow ,name='buy-now'),

path('paynow/', paynow ,name='paynow'),


path('verification/', include('verify_email.urls')),

path('search/',search,name='search'),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)