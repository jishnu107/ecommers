from django.shortcuts import render
from . models import Customer,Seller
import random
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def home_page(request):
    return render(request,'common/homepage.html')
def custreg_page(request):
    if request.method == 'POST': #when submit button is clicked
        c_name = request.POST['c_name'] #here we get data input in textbox,
        C_email = request.POST['c_email']
        c_address = request.POST['c_address']
        c_number = request.POST['c_number']
        c_gender = request.POST['c_gender']
        c_password = request.POST['c_password']
        #to insert data into table

        #1.craete object of model class, eg:Customer

        new_customer = Customer(Customer_name = c_name , Email_address = C_email,Address = c_address,Phone_number = c_number,Gender= c_gender,Cust_password=c_password)
         #call save() method, here save method is equalent to insert into sql query

        new_customer.save()
    return render(request,'common/custreg.html')

def sellreg_page(request):
    if request.method == 'POST':
        seller_name = request.POST['s_name']
        seller_email = request.POST['s_email']
        seller_address = request.POST['s_address']
        seller_number = request.POST['s_phone']
        gender = request.POST['s_gen']
        company_name = request.POST['comp_name']
        accholder = request.POST['accholder_name']
        branch = request.POST['s_branch']
        ifsc = request.POST['s_ifsc']
        seller_image = request.FILES['s_image']
        acc_number = request.POST['accnum']

        username = random.randint(1111,9999)
        seller_password = 'sel-' + seller_name.lower() + str(username)
        message = 'hai your username is ' + str(seller_name) + 'and temporary password is ' + seller_password


        send_mail(
            'username and temp password',
            message,
            settings.EMAIL_HOST_USER,
            [seller_email,],
            fail_silently=False
            
        )
        seller_list = Seller(seller_name = seller_name,seller_email = seller_email,Address = seller_address,Phone_number = seller_number, 
                      Gender = gender,comp_name = company_name,accholder_name = accholder, ifsc = ifsc,  branch = branch, acc_number=acc_number,
                      sell_pic = seller_image,seller_user = username,seller_pass =seller_password)
        seller_list.save()




    return render(request,'common/sellreg.html')
def selllogin_page(request):
    return render(request,'common/selllogin.html')
def addprod_page(request):
    return render(request,'common/addprod.html')
def custlogin_page(request):
    return render(request,'common/custlogin.html')
def pass_page(request):
    return render(request,'common/pass.html')