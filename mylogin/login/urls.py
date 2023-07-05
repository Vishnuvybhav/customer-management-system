"""mylogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.registerpage,name="register"),
    path('login/',views.loginpage,name="login"),
     path('logout/',views.logoutuser,name="logout"),
    path('',views.log,name='dashboard'),
    path('products',views.products,name="products"),
    path('createcustomer',views.createcustomers,name="createcustomer"),
    path('customer/<str:id>/',views.customers,name='customer'),
    path('order/<str:pk>/',views.orderview,name='order'),
    path('update_order/<str:pk>/',views.updateorder,name='update_order'),
    path('delete_order/<str:pk>/',views.deleteorder,name='delete_order'), 
]