from django.contrib import admin

# Register your models here.

from .models import customer,product,order,tag

admin.site.register(customer)
admin.site.register(order)
admin.site.register(product)
admin.site.register(tag)