# Generated by Django 3.2.16 on 2022-11-14 11:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=700, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WareHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
            options={
                'permissions': (('view_warehose', 'Can View Warehouse'), ('change_warehose', 'Can Change Warehouse'), ('add_warehose', 'Can Add Warehouse'), ('delete_warehose', 'Can Delete Warehouse')),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=700, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.warehouse')),
            ],
            options={
                'permissions': (('view_products', 'Can View Products'), ('change_products', 'Can Change Products'), ('add_products', 'Can Add Products'), ('delete_products', 'Can Delete Products')),
            },
        ),
    ]
