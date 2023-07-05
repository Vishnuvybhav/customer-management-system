from django.forms import ModelForm
from .models import product,customer,order
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class productform(ModelForm):
    class Meta:
        model=product
        fields='__all__'
class orderform(ModelForm):
    class Meta:
        model=order
        fields='__all__'
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class customerform(ModelForm):
    class Meta:
        model=customer
        fields='__all__'
        def _init_(self,*args,**kwargs):
            super()._init_(*args,**kwargs)
            for field in self.fields:
                new_data={
                    'class':'form-control'
                }
                
                self.fields[str(field)].widget.attrs.update(new_data)
        
