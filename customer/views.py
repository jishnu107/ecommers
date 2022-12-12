from django.shortcuts import render,redirect
from prodseller.models import Product
from common.models import Customer
from .models import Cart

# Create your views here.

def custhome_page(request):
    product_list = Product.objects.all()
    return render(request,'customer/custhome.html',{'prods': product_list})
def custpass_page(request):
    msg=''
    if request.method == 'POST':
        customer = Customer.objects.get(id = request.session['customer'])

        current_pass = request.POST['current_pass'] 
        new_pass = request.POST['new_pass'] 
        confirm_pass = request.POST['confirm_pass']

        if customer.Cust_password == current_pass:

            if new_pass == confirm_pass:
                 customer.Cust_password = new_pass
                 customer.save()
                 msg = 'Password changed succesfully'

            else:
                msg = 'Password does not match'

        else:
            msg = 'Incorrect Password'

    return render(request,'customer/pass.html',{'msg':msg})
def custorder_page(request):
    return render(request,'customer/order.html')
def custcart_page(request):
    product_cart = Cart.objects.all()
    return render(request,'customer/cart.html',{'cart_list':product_cart})
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