# Generated by Django 4.1.3 on 2022-12-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_seller_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Cust_password',
            new_name='cust_password',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Customer_name',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Email_address',
            new_name='email_address',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='seller',
            old_name='Phone_number',
            new_name='phone_number',
        ),
        migrations.AlterField(
            model_name='seller',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]