# Generated by Django 4.1.3 on 2022-12-03 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=20)),
                ('seller_email', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=100)),
                ('Phone_number', models.BigIntegerField()),
                ('Gender', models.CharField(max_length=50)),
                ('comp_name', models.CharField(max_length=100)),
                ('accholder_name', models.CharField(max_length=30)),
                ('ifsc', models.CharField(max_length=30)),
                ('branch', models.CharField(max_length=20)),
                ('seller_user', models.CharField(max_length=20)),
                ('seller_pass', models.CharField(max_length=20)),
                ('acc_number', models.BigIntegerField()),
                ('sell_pic', models.ImageField(upload_to='seller/')),
            ],
        ),
    ]
