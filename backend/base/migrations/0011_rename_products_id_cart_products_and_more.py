# Generated by Django 4.2.15 on 2024-09-01 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_product_product_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='products_id',
            new_name='products',
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='cart_id',
            new_name='cart',
        ),
        migrations.RenameField(
            model_name='orderdetail',
            old_name='product_id',
            new_name='product',
        ),
    ]
