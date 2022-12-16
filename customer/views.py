from django.shortcuts import render,redirect
from prodseller.models import Product
from common.models import Customer
from .models import Cart
from .auth_gaurd import auth_customer
# Create your views here.

@auth_customer
def custhome_page(request):
    product_list = Product.objects.all()
    return render(request,'customer/custhome.html',{'prods': product_list})

@auth_customer
def profile_page(request):
    msg=''
    product_list = Product.objects.all()
    if request.method=='POST':
        customer = Customer.objects.get(id = request.session['customer'])

        customer_name = request.POST['c_name']
        email_address = request.POST['c_email']
        address = request.POST['c_address']
        phone_number = request.POST['c_number']
        gender = request.POST['c_gender']

        customer.customer_name = customer_name
        customer.email_address = email_address
        customer.address = address
        customer.phone_number = phone_number
        customer.gender = gender
        customer.save()
        msg = 'Profile updated successfully'
    context = {
        'prods': product_list,
        'msg':msg
    }

    return render(request,'customer/profile.html',context)

@auth_customer
def custpass_page(request):
    msg=''
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        current_pass = request.POST['current_pass'] 
        new_pass = request.POST['new_pass'] 
        confirm_pass = request.POST['confirm_pass']

        if customer.cust_password == current_pass:

            if new_pass == confirm_pass:
                 customer.cust_password = new_pass
                 customer.save()
                 msg = 'Password changed succesfully'

            else:
                msg = 'Password does not match'

        else:
            msg = 'Incorrect Password'

    return render(request,'customer/pass.html',{'msg':msg})

@auth_customer
def custorder_page(request):
    return render(request,'customer/order.html')

@auth_customer
def custcart_page(request):
    # if 'customer' in request.session:
    product_cart = Cart.objects.filter(customer = request.session['customer'])
    return render(request,'customer/cart.html',{'cart_list':product_cart})
    # else:
    #     return redirect('common:custlogin')

@auth_customer
def viewproduct_page(request,pid):
    msg = ''
    product_details = Product.objects.get(id = pid)

    if request.method == 'POST':
        
        # checking if the user has added the same product in cart
        # exists() method  returns boolean value, true if data exists
        product_exist = Cart.objects.filter(product = pid,customer = request.session['customer'] ).exists()

        if not product_exist: # same as 'if product_exist == False'
            cart = Cart(customer_id = request.session['customer'],product_id = pid)
            cart.save()
            return redirect('customer:custcart')

        else:
            msg = 'Item already in cart'

        # data we pass from views to template is called context data
    context = {
        'details':product_details,
        'msg':msg
        }

    return render(request,'customer/viewproduct.html',context)

def remove_item(request,pid):
    cart_item = Cart.objects.get(product = pid,customer = request.session['customer'])
    cart_item.delete()
    return redirect('customer:custcart')

def logout(request):
    del request.session['customer'] 
    request.session.flush() #to remove session data from django_session table
    return redirect('common:custlogin')