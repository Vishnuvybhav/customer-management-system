from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import productform,orderform,createuserform,customerform
from django.contrib import messages
from .models import product,order,customer
from .filters import orderfilter

# Create your views here.
def registerpage(request):
    form = createuserform()

    if(request.method=='POST'):
       form = createuserform(request.POST)
       if form.is_valid():
          form.save()
          user = form.cleaned_data.get('username')
          messages.success(request,'Account created for ' + user)
          return redirect('login')

    context={'form':form}
    return render(request,'accounts/register.html',context)

def loginpage(request):
    if(request.method=='POST'):
      username = request.POST.get('username')  
      password = request.POST.get('password')  
      user = authenticate(request,username=username,password=password)
      if user is not None:
        login(request,user)
        return redirect('dashboard')
      else:
        messages.info(request,'Username or password is incorrect')
    context={}
    return render(request,'accounts/log.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def log(request):
    orders = order.objects.all()
    customers = customer.objects.all()
    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    context={'orders':orders,'customers':customers,'total_orders':total_orders,'delivered': delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)

def products(request):
    form = productform()
    data=product.objects.all()
    if(request.method=='POST'):
        form=productform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context={'form':form,'data':data}
    return render(request,'accounts/products.html',context)

def customers(request,id):
    customer1 = customer.objects.get(id = id)
    orders1 = customer1.order_set.all()
    order_count=orders1.count()
    myfilter = orderfilter(request.GET,queryset=orders1)
    orders1= myfilter.qs
    context = {'customer1':customer1,'orders1':orders1,'order_count':order_count,'myfilter':myfilter}
    return render(request,'accounts/customer.html',context)

def createcustomers(request):
    form2 = customerform()
    if request.method =='POST':
        form=customerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print("gxdfh")
    context={'form2':form2}
    return render(request,'accounts/createcustomer.html',context)


def orderview(request,pk):
    orderformset = inlineformset_factory(customer,order,fields=('product','status'),extra=5)
    customer1 = customer.objects.get(id=pk)
    formset = orderformset(queryset=order.objects.none(),instance=customer1)
    if(request.method=='POST'):
        formset = orderformset(request.POST,instance=customer1)
        if formset.is_valid():
            formset.save()
            return redirect('dashboard')
    context={'formset':formset}
    return render(request,'accounts/order.html',context)


def updateorder(request,pk):
    order1 = order.objects.get(id=pk)
    form=orderform(instance=order1)
    if request.method =='POST':
        form=orderform(request.POST,instance=order1)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context={'form':form}
    return render(request,'accounts/updateorder.html',context)

def deleteorder(request,pk):
    order1 = order.objects.get(id=pk)
    if(request.method=='POST'):
        order1.delete()
        return redirect('dashboard')
    context={'item':order1}
    return render(request,'accounts/delete.html',context)



