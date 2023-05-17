from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm

from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class registrationForm(UserCreationForm):
     password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
     password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
     email=forms.EmailField(required=True,label='Email id',widget=forms.EmailInput(attrs={'class':'form-control'}  ))
     first_name= forms.CharField(label='Enter first name',widget=forms.TextInput(attrs={'class':'form-control'}))
     last_name= forms.CharField(label='Enter last name',widget=forms.TextInput(attrs={'class':'form-control'}))

     class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}


class login(AuthenticationForm):
    username= UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=  forms.CharField( label='Password' ,strip=False ,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))


class passwordchange(PasswordChangeForm):
     old_password=  forms.CharField( label='Old Password' ,strip=False ,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','autofocus':True,'class':'form-control'}))
     new_password1=  forms.CharField( label='New Password' ,strip=False ,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
     new_password2 =  forms.CharField( label='Confirm Password' ,strip=False ,widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}))



class passswordreset(PasswordResetForm):
     email=forms.EmailField(required=True,label='Email id',max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}  ))


class setpassword(SetPasswordForm):
    new_password1= forms.CharField(label= "New Password" , strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password' , 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html() )
    new_password2= forms.CharField(label= "Confirm New Password" , strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password' , 'class':'form-control'}))


class Profile(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','address','phone','city','state','zipcode']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),'address':forms.TextInput(attrs={'class':'form-control'}),'phone': forms.NumberInput(attrs={'class':'form-control'}) , 'city':forms.TextInput(attrs={'class':'form-control'}), 'state':forms.Select(attrs={'class':'form-control'}), 'zipcode':forms.NumberInput(attrs={'class':'form-control'})}



class contactForm(forms.ModelForm):
 
     class Meta:
        model = contact
        fields = ['name','email','phone','content']
        widgets={ 
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}  ),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control','rows':'4'})
        }
