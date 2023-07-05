# Generated by Django 4.1.4 on 2023-01-27 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_customer_delete_temp'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_created', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('out for delivery', 'out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Indoor', 'Indoor'), ('out Door', 'out Door')], max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('Date_created', models.DateTimeField(null=True)),
            ],
        ),
    ]
