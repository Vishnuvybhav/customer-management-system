from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class customer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True);
    phone=models.CharField(max_length=200,null=True);
    email=models.EmailField(max_length=200,null=True);
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class tag(models.Model):
    name=models.CharField(max_length=200,null=True);

    def __str__(self):
        return self.name
   

class product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('out Door','out Door'),
    )
    name=models.CharField(max_length=200,null=True);
    price=models.FloatField(max_length=200,null=True);
    category=models.CharField(max_length=200,null=True,choices=CATEGORY);
    description=models.CharField(max_length=200,null=True,blank=True);
    Date_created=models.DateTimeField(auto_now_add=True,null=True);
    tag=models.ManyToManyField(tag)
    
    

    def __str__(self):
        return self.name


class order(models.Model):
    STATUS=(
           ('Pending','Pending'),
           ('out for delivery','out for delivery'),
           ('Delivered','Delivered'),
           )
    customer=models.ForeignKey(customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)
    Date_created=models.DateTimeField(auto_now_add=True,null=True);
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    
    def __str__(self):
         return self.product.name
