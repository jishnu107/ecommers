from django.shortcuts import render,redirect
from . models import Customer,Seller
import random
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.

def home_page(request):
    return render(request,'common/selllogin.html')

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
        message = 'hai your username is ' + str(username) + 'and temporary password is ' + seller_password


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
    msg = ''
    if request.method == 'POST':
        sell_username = request.POST['s_username'] 
        sell_password = request.POST['sell_password'] 
        
        # select * from seller where selleruname= selername and passwd = passwd
        try :
            seller = Seller.objects.get(seller_user = sell_username, seller_pass = sell_password )

            # if username and password is correct, we set a session variable with key 'seller'
            # session variable can be accessed throughout the application

            # working of django session
            # when username and password is correct, we set a session variable with key(here key is 'seller') and
            # unique value for each seller (here value is the primary key of the logged in seller)
            # if a seller with primary key 2 logs in, session key will be 'seller' and value will be 2
            
            # when we set a session, key and value will be stored in django_session table inside database in encrypted format

            # the encrypted key will be send with http response to the client (browser)
            # in the client side (browser), the key received from the server will be stored in browser storage (cookies in case of django)

            # when the user request any page (eg : cart page) from the same browser, the same key stored inside cookies
            # will be sending to the server through http request 

            # when the request reaches the server, it will look for the key stored in cookie to match with 
            # django_session table inside the database to find the corresponding user


            request.session['seller'] = seller.id
            return redirect('reseller:sellerhome')
        except:
             msg = 'username or password incorrect'
    return render(request,'common/selllogin.html',{'msg':msg})
def addprod_page(request):
    return render(request,'common/addprod.html')
def custlogin_page(request):
    return render(request,'common/custlogin.html')
def pass_page(request):
    return render(request,'common/pass.html')