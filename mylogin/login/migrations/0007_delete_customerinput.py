# Generated by Django 4.1.4 on 2023-01-30 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_order_customer_alter_order_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customerinput',
        ),
    ]